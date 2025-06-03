from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def data_one_station_one_date(station, date):
    filename_station = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    data_station = pd.read_csv(filename_station,
                               skiprows=20,
                               parse_dates=["    DATE"])
    temperature = data_station.loc[data_station["    DATE"] == date]["   TG"].squeeze() / 10

    return {"station": station,
            "date": date,
            "temperature": temperature}


@app.route("/api/v1/<station>")
def all_data_one_station(station):
    filename_station = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    data_station = pd.read_csv(filename_station,
                               skiprows=20,
                               parse_dates=["    DATE"])

    return data_station.to_dict(orient="records")


@app.route("/api/v1/yearly/<station>/<year>")
def all_data_one_year(station, year):
    filename_station = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    data_station = pd.read_csv(filename_station, skiprows=20)
    data_station["    DATE"] = data_station["    DATE"].astype(str)
    data_year = data_station[data_station["    DATE"].str.startswith(str(year))]

    return data_year.to_dict(orient="records")


if __name__ == "__main__":
    app.run(debug=True, port=5001)