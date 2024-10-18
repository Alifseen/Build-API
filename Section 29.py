"""Build a REST API with an HTML Documentation Page
"""
## 1. Imported Flask function (to process app) and Render template (show html) function from flask
from flask import Flask, render_template
import pandas as pd

## 2. initiated the Flask function in a variable
app = Flask(__name__)


## 3. Created a home page by routing a link to render an HTML file in templates folder
@app.route("/")
def home():
    return render_template("Home.html")


## 5. Created an endpoint to return a dictionary with temperature values from data
@app.route("/api/v1/<station>/<date>")  ## Dynamically get the station and date from url
def endpoint(station, date):
    ## 6. read the file from a folder containing 6500 files for each station, format the filepath string to dynamically get station id from url
    df = pd.read_csv(r"D:\Downloads\European_weather_data-all\TG_STAID" + station.zfill(6) + ".txt",
                     ## 7. skip 20 rows, since we opened a txt file which has text in first 20 lines, csv starts from line 21
                     skiprows=20,
                     ## 8. instruct pandas to read the column named "DATE" as date
                     parse_dates=["    DATE"])
    ## 9. Store the value of the Temperature stored in "TG" column of the same row where date matches
    temp = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    ## 10. Return values as a JSON
    return {"Station No.": station,
            "Date": date,
            "Temperature": temp}


## 4. Run the app on port 5001 with debug on, only when this script is run.
if __name__ == "__main__":
    app.run(debug=True)
