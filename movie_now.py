from flask import Flask
from flask import render_template
from flask import request
import search_movies as sm

app = Flask(__name__)

@app.route('/')
def hello_movie():
    return render_template('index.html')

@app.route("/searching.html")
def searching():
    actors = request.args.get("actors")
    rating = request.args.get("rating")
    genre = request.args.get("genre")
    content = sm.searching(genre=genre.lower(),rating=rating)
    # movie, rating, img = 
    movie = sm.get_movie(content)
    # print(actors, rating, genre)
    return render_template("searching.html",movie=movie)

if __name__ == "__main__":
    app.run(debug=True)