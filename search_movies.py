import requests
from bs4 import BeautifulSoup

def searching(genre="action-and-adventure", rating="0", year="1900", movie_or_tvshow="movies", streamer="netflix"):
    
    try:
        response = requests.get(f"https://reelgood.com/{movie_or_tvshow}/genre/{genre}/{streamer}?filter-imdb_start={rating}&filter-sort=2")
    except:
        print("We can't find any movies :( Please, try again!")
    else:
        return response.content
    finally:
        print("We can't find any movies :( Please, try again!")
        # response = requests.get("https://reelgood.com/movies/")
    return {"key":"Nothing to show"}