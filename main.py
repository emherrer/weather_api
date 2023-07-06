from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


data = pd.read_csv("data/stations.txt", skiprows=17)
data = data[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    return render_template("home.html", data=data.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filepath = "data//TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filepath, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}

if __name__ == "__main__":
    app.run(debug=True)
