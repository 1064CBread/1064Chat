"""
Utilities specific to REST blueprints.
"""
from enum import Enum
from util import get_current_app
from functools import wraps
import re


class ClientType(str, Enum):
    BROWSER = "browser"  # most useful in debug
    CURL = "cURL"  # also useful in debug
    OTHER = "other"  # usually production apps


browsers = re.compile("|".join(("chrome", "firefox", "safari", "opera")), re.IGNORECASE)


def get_implied_client_type(useragent: str) -> ClientType:
    """
    Attempts to get the client type based on user-agent. This is by no means exaustive for browser checking,
    and may be incorrect if the client lies.
    :param useragent: The user-agent that the client provided
    :return: The ClientType the user-agent implies
    """
    if browsers.search(useragent):
        return ClientType.BROWSER
    if "curl/" in useragent:
        return ClientType.CURL
    return ClientType.OTHER


_shared_decorator_key = __name__ + "_shared_decorator"


def _shared_decorator_logic(**response_kwargs):
    """
    Shared deco logic, merges decorators that are used together
    """

    def make_wrapper(f):
        merged_kwargs = response_kwargs.copy()
        fn = f
        if hasattr(f, _shared_decorator_key):
            data = getattr(f, _shared_decorator_key)
            merged_kwargs.update(data['kwargs'])
            fn = data['wrapped']

        @wraps(fn)
        def wrapper(*args, **kwargs):
            return get_current_app().response_class(fn(*args, **kwargs), **merged_kwargs)

        setattr(wrapper, _shared_decorator_key, {'kwargs': merged_kwargs, 'wrapped': f})
        return wrapper

    return make_wrapper


def content_type(ctype):
    return _shared_decorator_logic(content_type=ctype)


def status_code(code):
    return _shared_decorator_logic(status=code)


def headers(direct_dict=None, **kwargs):
    funneled = direct_dict or dict()
    funneled.update(kwargs)
    funneled = {k.replace('_', '-').upper(): v for k, v in funneled.items()}
    return _shared_decorator_logic(headers=funneled)
