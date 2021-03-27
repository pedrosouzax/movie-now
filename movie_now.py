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
    rating = request.args.get("rating")
    genre = request.args.get("genre")
    streamer = request.args.get("streamer")
    # movie_tvshow = request.args.get("movie-tvshow")
    content = sm.searching(genre=genre.lower(),rating=rating,streamer=streamer)
    name,folder,year,imdb = sm.get_movie(content)
    # print(actors, rating, genre)
    return render_template("searching.html",title=name,folder=folder, year=year, imdb=imdb)

if __name__ == "__main__":
    app.run(debug=True)