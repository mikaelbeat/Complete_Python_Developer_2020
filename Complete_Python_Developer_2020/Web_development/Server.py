
# Create virtual environment
# Folders bin / include / lib
# py -3 -m venv location

# Setup flask to run specific script
# set FLASK_APP=Server.py

# Set debug mode on
# set FLASK_ENV=development

# Run flask app
# flask run


from flask import Flask, render_template

app = Flask(__name__)

print(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)
