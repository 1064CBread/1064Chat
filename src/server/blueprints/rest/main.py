from flask import Blueprint, current_app, Flask, render_template, url_for

blueprint = Blueprint(__name__, __name__, url_prefix='/rest')


@blueprint.route('/')
def index():
    return ""

def registerself(app: Flask, prefix=''):
    app.register_blueprint(blueprint, prefix=prefix + blueprint.url_prefix)
