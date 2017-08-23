#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import json

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    @app.route("/")
    def index():
        return json.dumps({"status":"ok"})

    return app
