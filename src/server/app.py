#!/usr/bin/env python3
from flask import Flask
from common.constants import *
from pathlib import Path
import os
import sys
sys.path.append(str(Path(__file__).parent))

app = Flask(PROGRAM_NAME)

addr = os.environ.get(PROGRAM_NAME.upper() + '_SERVER_ADDRESS', '0.0.0.0')
port = os.environ.get(PROGRAM_NAME.upper() + '_SERVER_PORT', DEFAULT_PORT)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='https://www.youtube.com/watch?v=zwZISypgA9M'
))
app.config.from_envvar(PROGRAM_NAME.upper() + '_SETTINGS', silent=True)


@app.route('/')
def index():
    links = ["/webui/", "/rest/"]
    htmllinks = ['<a href="{0}">{0}</a>'.format(x) for x in links]
    return "Either go to " + " or ".join(htmllinks)

def run():
    from blueprints import webui
    from blueprints.rest import main as restmain

    restmain.registerself(app)
    webui.registerself(app)
    app.run(addr, port)
