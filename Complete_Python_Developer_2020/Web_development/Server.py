
# Create virtual environment
# py -3 -m venv location

from flask import Flask, render_template

app = Flask(__name__)

print(__name__)


@app.route("/<username>/<int:id>")
def start_page(username=None, id=None):
    return render_template("index.html", name=username, id=id)

@app.route("/about.html")
def blog_page():
    return render_template("about.html")

@app.route("/blog/2020/cats")
def blog_page2():
    return "This is a blog page about cats!"