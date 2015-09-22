#!/usr/bin/env python3

from pathlib import Path

from flask import Flask
from common.constants import *
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
def index():
    return "Nothing to see."


if __name__ == '__main__':
    from blueprints import security
    app.register_blueprint(security.blueprint)
    app.run(addr, port)
