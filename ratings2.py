from pymongo import MongoClient
import genre
import code
#1. Connecting Mongo DB
client = MongoClient('localhost', 27017)
db = client.mydb			#Getting Database

# This will give list of movie ids  from IMDB
collection = db.movies		# Getting Collection
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
genre_collection = db.mygenres		# Getting Collection
mygenres_cursor = genre_collection.find()
my_genre_list = []
for mygenre in mygenres_cursor:
	my_genre_list.append(mygenre['rating'])



user_types = code.final
#movie_id_list
#movie_genre_list
#my_genre_list


# for i in movie_genre_list:
# 	for j in my_genre_list:
# 		imdb = i.split("|")
# 		genre = j.split("|")
# 		l = []
# 		for m in genre:
# 			for n in imdb:
# 				if m.find(n) >= 0:
# 					m = m + "," + m
# 					l = m.split(",")
# 		l = l[::2]
# 		l = map(float,l)
# 		#rating = None
# 		count = 0
# 		if len(l)>0:
# 			rating = sum(l)/len(l)
# 			#print rating
# 		l = []




count = 1

for user in user_types:
	print user
 	for movie_id in movie_id_list:
 		imdb_genre = None
 		print movie_id
 		k = collection.find( {"movieId":movie_id } )
		for i in k:
			imdb_genre =  i['genres']
 		i = imdb_genre
 		print i
		for j in my_genre_list:
			imdb = i.split("|")
			genre = j.split("|")
			l = []
			for m in genre:
				for n in imdb:
					if m.find(n) >= 0:
						m = m + "," + m
						l = m.split(",")
			l = l[::2]
			l = map(float,l)
			#rating = None
			count = 0
			if len(l)>0:
				rating = sum(l)/len(l)
			print rating
			l = []





