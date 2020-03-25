
# Create virtual environment
# Folders bin / include / lib
# py -3 -m venv location

# Setup flask to run specific script
# set FLASK_APP=Server.py

# Set debug mode on
# set FLASK_ENV=development

# Run flask app
# flask run


from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

print(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        return redirect("/thankyou.html")
    else:
        return "Something went wrong. Try Again!"
