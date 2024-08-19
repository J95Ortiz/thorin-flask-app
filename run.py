# Imports os from the python library.
import os

# Imports the json library as we'll use this to pull the members' data
import json

# Imports the Flask class, and render_template which displays the file assigned to it.
from flask import Flask, render_template, request, flash

if os.path.exists("env.py"):
    import env


# Creates an instance of the Flask class and stores it in the "app" variable.
# The first argument of the Flask class is the name of the application's module/package.
# Since we're just using a single module, we can use __name__ which is a built-in Python variable.
# Flask needs this so it knows where to look for templates and static files.
app = Flask(__name__)   
app.secret_key = os.environ.get("SECRET_KEY")


# The route decorator tells the app which URL should trigger the fn.
# This routing will open the index.html file
@app.route("/")     
def index():
    return render_template("index.html")


# This routing will open the index.html file
@app.route("/about")     
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company = data)


# This will create a separate page for each member by taking the url attribute in company.json
@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


# This routing will open the contact.html file
@app.route("/contact", methods=["GET", "POST"])     
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")

# This routing will open the careers.html file
@app.route("/careers")     
def careers():
    return render_template("careers.html", page_title="Careers")


# "__main__" is the name of the default module in Python
if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug = True) # Make sure debug = True is removed before any submission.

# {{ }} is for inserting content (in this case, straight into the href)
# {% %} is for elements which affect the flow of the page
# The lines below create a template which can be inserted into other similar pages to avoid repetitiveness