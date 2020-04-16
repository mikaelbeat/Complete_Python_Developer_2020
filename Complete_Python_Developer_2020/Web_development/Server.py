
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
import csv

app = Flask(__name__)

print(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email}, {subject}, {message}")

def write_to_csv_file(data):
    with open("database.csv", newline="", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=",",  quotechar="|", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            print(data)
            write_to_file(data)
            write_to_csv_file(data)
            return redirect("/thankyou.html")
        except:
            return "Error while saving to database!"
    else:
        return "Something went wrong. Try Again!"
