import requests
from bs4 import BeautifulSoup

def searching(genre="all", rating="0", year="1900", movie_or_tvshow="movies", streamer="netflix"):
    
    try:
        if genre == "all":
            response = requests.get(f"https://reelgood.com/{movie_or_tvshow}/source/{streamer}?filter-imdb_start={rating}&filter-sort=2")
            return response.content
        else:
            print(f"https://reelgood.com/{movie_or_tvshow}/genre/{genre}/on-{streamer}?filter-imdb_start={rating}&filter-sort=2")
            response = requests.get(f"https://reelgood.com/{movie_or_tvshow}/genre/{genre}/on-{streamer}?filter-imdb_start={rating}&filter-sort=2")
            return response.content
    except:
        return "We can't find any movies :( Please, try again!"

def get_movie():
    pass