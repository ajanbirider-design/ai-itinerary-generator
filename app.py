from flask import Flask, render_template, request
from planner import generate_plan
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    plan = None
    weather = None
    map_link = None

    if request.method == "POST":
        destination = request.form["destination"]

        if destination == "Other":
            destination = request.form["custom_destination"]

        budget = request.form["budget"]
        days = request.form["days"]
        mode = request.form["mode"]

        plan, weather = generate_plan(destination, budget, days, mode)

        map_link = f"https://www.google.com/maps/search/?api=1&query={destination}"

    return render_template("index.html", plan=plan, weather=weather, map_link=map_link)


if __name__ == "__main__":
    app.run(debug=True)
