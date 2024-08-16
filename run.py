# Imports os from the python library.
import os

# Imports the Flask class, and render_template which displays the file assigned to it.
from flask import Flask, render_template     


# Creates an instance of the Flask class and stores it in the "app" variable.
# The first argument of the Flask class is the name of the application's module/package.
# Since we're just using a single module, we can use __name__ which is a built-in Python variable.
# Flask needs this so it knows where to look for templates and static files.
app = Flask(__name__)   


# The route decorator tells the app which URL should trigger the index() fn.
@app.route("/")     
def index():
    return render_template("index.html")

@app.route("/about")     
def about():
    return render_template("about.html")


# "__main__" is the name of the default module in Python
if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug = True) # Make sure debug = True is removed before any submission.