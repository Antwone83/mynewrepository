#!/usr/bin/env python3
# -*_ coding: utf8 -*-
"""Sample hello world Flask App"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1> HEllo, wolrd<h1>"


@app.route("/products")
def products():
    product_list = ["Apples", "Oranges", "Bananas"]
    bullet_list = "".join(
        "<li>%s</li>" % product for product in product_list
        )
    return "<ul>%s</ul>" % bullet_list

@app.route("/aboutme")
def about_me():
    me = {
        "first_name": "Antwone",
        "last_name": "Adams",
        "hobbies": "DIY stuff"
    }
    return me