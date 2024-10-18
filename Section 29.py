"""Build a REST API with an HTML Documentation Page
"""
## 1. Imported Flask function (to process app) and Render template (show html) function from flask
from flask import Flask, render_template

## 2. initiated the Flask function in a variable
app = Flask(__name__)


## 3. Created a home page by routing a link to render an HTML file in templates folder
@app.route("/")
def home():
    return render_template("Home.html")

## 4. Run the app on port 5001 with debug on, only when this script is run.
if __name__ == "__main__":
    app.run(debug=True, port=5001)