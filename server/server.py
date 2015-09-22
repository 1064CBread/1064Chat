#!/usr/bin/env python3

from generated_protobuf.user_pb2 import User
from flask import Flask, Response, request
from http import HTTPStatus
from common.constants import *
from pathlib import Path, PurePath
import os

app = Flask(PROGRAM_NAME)

addr = os.environ.get(PROGRAM_NAME.upper() + '_SERVER_ADDRESS', '0.0.0.0')
port = os.environ.get(PROGRAM_NAME.upper() + '_SERVER_PORT', DEFAULT_PORT)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='https://www.youtube.com/watch?v=zwZISypgA9M'
))
app.config.from_envvar(PROGRAM_NAME.upper() + '_SETTINGS', silent=True)

base_path = Path(__file__).parent


@app.route('/')
@app.route('/<path:path>')
def index(path='.'):
    p = Path.cwd() / path
    parent = str(PurePath('/' + path).parent)
    dotdot = ('<li><a href="' + parent + '">..</a>')
    if not p.exists():
        return Response('404<ul>' + dotdot, 404)
    if p.is_dir():
        return (('/' if path == '.' else path) + '<ul>' +
                '<li>'.join('<a href="/' + ('' if path == '.' else path + '/') + y + '">' + y + '</a>' for y in
                            (str(x.relative_to(p)) for x in p.iterdir())) +
                dotdot +
                '</ul>')
    try:
        return Response((Path.cwd() / path).read_text(), content_type='text/plain')
    except UnicodeDecodeError:
        return Response("No. Stop that.<ul>" + dotdot, HTTPStatus.UNAUTHORIZED)


if __name__ == '__main__':
    from blueprints import security

    app.register_blueprint(security.blueprint)
    app.run(addr, port)
