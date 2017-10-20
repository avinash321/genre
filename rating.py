'''
This will construct a ratings excel sheet
'''
from pymongo import MongoClient
import genre
import code
# Getting Genres based on given personality code
#mygenre = genre.get_genre("LAAAH")
#print mygenre     # ex: ['independent (3.59)', 'war (3.51)', 'science fiction (3.55)', 'adventure (3.56)']
# Getting movie collection from mongodb
# Going to create UsrID & movieid & rating dataset
client = MongoClient('localhost', 27017)
db = client.mydb		#Getting Database
collection = db.movies		# Getting Collection
movie_cursor = collection.find()


genre_collection = db.mygenres		# Getting Collection
mygenres_cursor = genre_collection.find()

user_types = code.final
print user_types


user_genre = []
for mygenres in mygenres_cursor:
		user_genre = mygenres['movieId']
		user_genre = user_genre.split(',')

		#print  user_genre
		user_genre.append(mygenres['movieId'])
# imdb_genre = {}
# imdb_movieId = {}
# imdb_title = {}
# for movies_dict in movie_cursor:
# 	print movies_dict
# 	#print movies_dict['title']
# 	#print movies_dict['movieId']
# 	#print movies_dict['genres']
# 	imdb_genre = imdb_genre.update(movies_dict['genres'])
# 	imdb_movieId = imdb_movieId.update(movies_dict['movieId'])
# 	imdb_title =imdb_title.update(movies_dict['title'])
# 	#if temp_genre.find('')

# user_types = code.final
# print user_types
# genre_collection = db.mygenres		# Getting Collection
# mygenres_cursor = genre_collection.find()



# for mygenres in mygenres_cursor:
# 	#user_genre = mygenres['rating']
# 	user_genre = mygenres['movieId']

#user_genre = user_genre.split(",")
#print user_genre


# for user in user_types:
# 	for mygenres in mygenres_cursor:
# 		user_genre = mygenres['movieId']
# 		user_genre = user_genre.split(",")
# 		#print user_genre
# 		for genre in user_genre:
# 			for movies_dict in movie_cursor:
# 				k = movies_dict['genres']
# 				#print k
# 				#if temp_genre.find('')
# 				if k.find(genre) >= 0:
# 					print genre
# 					print user
# 					print "success"
# 					break

# Lets pay with usertype
# 1 Lets take mygenre 

#print user_genre




			



# for i in user_type:
# 	for j in mygenre:
# 		if 

	# for movie_dict in movies_obj:
	# 	print movies_obj[movie_dict]

# Printing all movies based on genre
#for i in mygenre:
	#for j in 



