from flask import current_app, url_for
from collections.abc import Container
from werkzeug.routing import Rule
from typing import Iterable


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


def get_rules(filt=lambda x: True) -> Iterable[Rule]:
    """

    :param filt: either list of names to check if the endpoint contains or a filter function
    :return:
    """
    fn = filt
    if isinstance(filt, Container):
        fn = lambda x: any((name in x.endpoint) for name in filt)
    return [x for x in current_app.url_map.iter_rules()
            if "GET" in x.methods and has_no_empty_params(x) and fn(x)]
