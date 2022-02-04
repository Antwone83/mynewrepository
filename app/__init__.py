#!/usr/bin/env python3
# -*_ coding: utf8 -*-
"""Sample hello world Flask App"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1> HEllo, wolrd<h1>"