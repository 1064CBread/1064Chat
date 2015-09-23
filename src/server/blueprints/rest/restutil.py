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


def _shared_decorator_logic(**response_kwargs):
    def make_wrapper(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return get_current_app().response_class(f(*args, **kwargs), **response_kwargs)

        return wrapper

    return make_wrapper


def content_type(ctype):
    return _shared_decorator_logic(content_type=ctype)
