from  flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_movie():
    return render_template('index.html')

@app.route("/searching.html")
def searching():
    actors = request.args.get("actors")
    rating = request.args.get("rating")
    genre = request.args.get("genre")
    print(genre,rating,actors)
    return render_template("index.html")