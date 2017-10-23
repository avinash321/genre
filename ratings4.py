from pymongo import MongoClient
import genre
import code
import random
from multiprocessing import Process,Manager

#1. Connecting Mongo DB
client = MongoClient('localhost', 27017)
db = client.mydb            #Getting Database

# This will give list of movie ids  from IMDB
collection = db.movies      # Getting Collection
movie_cursor = collection.find()
movie_id_list = []
for movie in movie_cursor:
    movie_id_list.append(movie['movieId'])

# this will give list of genres from IMDB
movie_cursor = collection.find()
movie_genre_list = []
for genre in movie_cursor:
    movie_genre_list.append(genre['genres'])


# THis will give list of genres with personality based ratings
genre_collection = db.mygenres      # Getting Collection
mygenres_cursor = genre_collection.find()
my_genre_list = []
for mygenre in mygenres_cursor:
    my_genre_list.append(mygenre['rating'])



user_types = code.final
#movie_id_list
#movie_genre_list
#my_genre_list


def rate_caliculator(movie_id,return_dict):
    imdb_genre = collection.find( {"movieId":movie_id } )
    k =None
    for i in imdb_genre:
        k =  i["genres"]

    for my_genre in my_genre_list:
        imdb = k.split("|")
        genre = my_genre.split("|")
        l = []
        for m in genre:
            for n in imdb:
                if m.find(n) >= 0:
                    m = m + "," + m
                    l = m.split(",")
        l = l[::2]
        l = map(float,l)
        if len(l)>0:
            rating = sum(l)/len(l)
            return_dict[rating] = rating
            #return rating
        l = []

count = 0
for user in user_types:
    count = count + 1
    movie_id_list = random.sample(movie_id_list, 100)
    manager = Manager()
    return_dict = manager.dict()
    jobs = []


    for movie_id in movie_id_list:
        p = Process(target=rate_caliculator, args=(movie_id,return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    print return_dict.values()


    # for movie_id in movie_id_list:
    #   rate = Process(target=rate_caliculator, args=(movie_id,))
    #   #rate = rate_caliculator(movie_id)
    #   if rate is not None:
    #       print count,movie_id,rate
            #test_col = db.test
            #test_col.insert_one({"userId":count, "movieId":movie_id, "rating":rate,"timestamp":"847117005"})

# Preparing an excel Sheet with user types along with those genre types
