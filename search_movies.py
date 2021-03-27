import requests
from bs4 import BeautifulSoup
import random

def searching(genre="all", rating="0", year="1900", movie_or_tvshow="movies", streamer="netflix"):
    
    try:
        if genre == "all":
            response = requests.get(f"https://reelgood.com/{movie_or_tvshow}/source/{streamer}?filter-imdb_start={rating}&filter-sort=2")
            return response.content
        else:
            print(f"https://reelgood.com/{movie_or_tvshow}/genre/{genre}/on-{streamer}?filter-imdb_start={rating}&filter-sort=2")
            response = requests.get(f"https://reelgood.com/{movie_or_tvshow}/genre/{genre}/on-{streamer}?filter-imdb_start={rating}&filter-sort=2")
            print("aaaa")
            return response.content
    except:
        return "We can't find any movies :( Please, try again!"

def get_movie(content):
    soup =  BeautifulSoup(content,'html.parser')
    movies_list = []
    movies_list = [soup.find_all("tr",class_="css-o6sgwe")[x] for x in range(len(soup.find_all("tr",class_="css-o6sgwe")))]
    #print(movies_list,"\n\n")
    movie_tr = random.choice(movies_list)
    movie_name = movie_tr.find("td",class_="css-1u7zfla e126mwsw1").a.string
    movie_folder = movie_tr.find("picture", class_="css-b4kcmh e1181ybh0").img["src"]
    movie_year = movie_tr.find("td",class_="css-1u11l3y").string
    movie_imdb = movie_tr.find("b",class_="css-1px39yc").div.span.b.string
    # movie_avaliable = movie_tr.find("td", class_="css-1vuzpp2").span.div.img["alt"]
    # print(movie_name,"\n\n")
    # print(movie_year,"\n\n")
    # print(movie_imdb,"\n\n")
    # print(movie_folder,"\n\n")
    return movie_name,movie_folder, movie_year,movie_imdb
    