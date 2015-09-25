from flask import Blueprint, Flask, render_template, url_for
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
    from util import get_rules

    d = dict()
    d['PageData'] = constants.PageData
    rules = get_rules([security.blueprint.name, blueprint.name])
    # sorts endpoints by last segment (e.x. f.o.o is sorted using o)
    endpoints = list(sorted(((x.endpoint, x.endpoint.split('.')[-1]) for x in rules), key=lambda x: x[1]))
    d['allpages'] = tuple((url_for(k), v, titlecase(v)) for k, v in endpoints)
    d['navbar_should_show_page'] = lambda x: True
    d['custom_css'] = [ "/static/webui.css" ]
    d['get_channels'] = get_channels
    return d


def registerself(app: Flask, prefix=''):
    prefix += blueprint.url_prefix
    app.register_blueprint(blueprint, url_prefix=prefix)
    security.registerself(app, prefix=prefix)

def get_channels():
    # TODO store which channels a user is talking in, and return them here
    return ["1064CBread", "Other Conversation", "Foobar"]
