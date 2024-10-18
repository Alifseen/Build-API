from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")


## Improvement by looking at instructors code: Instead of creating this df everything the url is hit, we create it only once since this is a static file and does not change, only when data changes, do you need to create a dataframe when endpoint is called.
df = pd.read_csv("Files/dictionary.csv")


@app.route("/api/v1/<word>")
def api(word):
    definition = df.loc[df["word"] == word]["definition"].squeeze()
    return {
        "definition": definition,
        "word": word
    }


if __name__ == "__main__":
    app.run(debug=True, port=5001)