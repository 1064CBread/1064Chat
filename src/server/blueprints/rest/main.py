from blueprints.rest import restutil
from flask import Blueprint, current_app, Flask, request, Response, url_for
import json
import util

blueprint = Blueprint(__name__, __name__, url_prefix='/rest')


@blueprint.route('/')
def index():
    urls = dict(urls=[url_for(x.endpoint) for x in util.get_rules([blueprint.name])])
    client_type = restutil.get_implied_client_type(request.user_agent.string)
    client_is_other = client_type == restutil.ClientType.OTHER
    return Response(json.dumps(urls, sort_keys=not client_is_other, indent=2 - (client_is_other * 2)),
                    content_type='text/json')


def registerself(app: Flask, prefix=''):
    app.register_blueprint(blueprint, prefix=prefix + blueprint.url_prefix)
