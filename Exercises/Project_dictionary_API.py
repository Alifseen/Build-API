from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/api/v1/<word>")
def api(word):
    df = pd.read_csv("Files/dictionary.csv")
    definition = df.loc[df["word"] == word]["definition"].squeeze()
    return {
        "definition": definition,
        "word": word
    }


if __name__ == "__main__":
    app.run(debug=True, port=5001)