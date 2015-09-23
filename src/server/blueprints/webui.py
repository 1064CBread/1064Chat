from flask import Blueprint, current_app, Flask, render_template, url_for
from blueprints import security

blueprint = Blueprint(__name__, __name__, url_prefix='/webui')


@blueprint.route('/')
def index():
    return render_template('index.jinja')


@blueprint.app_template_filter('index')
def filter_index(m, v):
    return m[v]


@blueprint.app_context_processor
def add_jinja_vars():
    import constants
    from titlecase import titlecase

    def has_no_empty_params(rule):
        defaults = rule.defaults if rule.defaults is not None else ()
        arguments = rule.arguments if rule.arguments is not None else ()
        return len(defaults) >= len(arguments)

    d = dict()
    d['PageData'] = constants.PageData
    rules = [x for x in current_app.url_map.iter_rules()
             if "GET" in x.methods and has_no_empty_params(x) and
             (blueprint.name in x.endpoint or security.blueprint.name in x.endpoint)]
    # sorts endpoints by last segment (e.x. f.o.o is sorted using o)
    endpoints = list(sorted(((x.endpoint, x.endpoint.split('.')[-1]) for x in rules), key=lambda x: x[1]))
    d['allpages'] = tuple((url_for(k), v, titlecase(v)) for k, v in endpoints)
    d['navbar_should_show_page'] = lambda x: True
    return d


def registerself(app: Flask, prefix=''):
    prefix += blueprint.url_prefix
    app.register_blueprint(blueprint, url_prefix=prefix)
    security.registerself(app, prefix=prefix)
