from cs50 import SQL
from flask import Flask, render_template, request
from helpers import random_string
import random

app = Flask(__name__)

db = SQL("sqlite:///history.db")

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        page = request.form.get("page")
        try :
            page = int(page)
        except ValueError:
            return render_template("index.html", random_string="Enter a number")

        if (page < 0):
            return render_template("index.html", random_string="Type in a positive number")
        random.seed(page)
        db.execute("INSERT INTO history (page) VALUES(?)", page)
    string = random_string(1000)
    rows = db.execute("SELECT * FROM history;")
    print(rows)
    return render_template("index.html", random_string=string, history=rows )
