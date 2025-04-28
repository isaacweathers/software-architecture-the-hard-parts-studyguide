#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

@app.route("/about")
def about():
    return app.send_static_file("about.html")

@app.route("/diagrams")
def diagrams():
    return app.send_static_file("diagrams.html")

@app.route("/contact")
def contact():
    return app.send_static_file("contact.html")
