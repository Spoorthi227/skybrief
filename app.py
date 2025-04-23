from flask import Flask, render_template, request
from weather_utils import generate_weather_summary

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        route = request.form.get("route")
        if route:
            summary = generate_weather_summary(route)
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
