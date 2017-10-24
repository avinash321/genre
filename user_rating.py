'''
This will generate the CSV File with the columns "userId", "movieId", and "rating" (In MongoDB)
We can use/replace this File directly in lenskit recommendation Engine.
Based on this we can recommend top 10 recommndations of a respective user(type)
'''
from pymongo import MongoClient
import genre
import random
from user_codes import users

#Connecting Mongo DB
client = MongoClient('localhost', 27017)
db = client.genre			#Getting Database (genre)

# This will get the list of moviId's from IMDB
imdb_cursor = db.imdb_genres.find()
movie_id_list = []
for cursor_obj in imdb_cursor:
	movie_id_list.append(cursor_obj['movieId'])

# this will get list of Genres from IMDB
imdb_cursor = db.imdb_genres.find()
imdb_genre_list = []
for cursor_obj in imdb_cursor:
	imdb_genre_list.append(cursor_obj['genres'])

# THis will give list of genres with personality based ratings
user_cursor = db.user_genres.find()
user_genre_list = []
for cursor_obj in user_cursor:
	user_genre_list.append(cursor_obj['genres'])


def movie_rating_calc(movie_id):
	'''
	Parameters:
		movie_id: It will take the movie_id as input
	Description:
		in the following way this caliculation will perform,
		1) First it will fetch the concerned movie_id object form the imdb_genre collectiion,
		  Based on given movie Id.
		2) Then It will compare the given Imdb genre with all the user genres
		3) If the genres were match, then it will take the matched genre rating,
		   If there are more number of matches then it will take the Average
	Return:
		It will Returns the rating for the given movieId (movie)
	'''
	imdb_movieId_cursor = db.imdb_genres.find( {"movieId":movie_id } )
	imdb_genre = None
	for cursor_obj in imdb_movieId_cursor:
		imdb_genre =  cursor_obj["genres"]
	imdb = imdb_genre.split("|")

	# This is how we rate a movie
	for user_genre in user_genre_list:
		user = user_genre.split("|")
		temp_list = []
		for u_genre in user:
			for im_genre in imdb:
				if u_genre.find(im_genre) >= 0:
					u_genre = u_genre + "," + u_genre
					temp_list = u_genre.split(",")
		temp_list = temp_list[::2]
		temp_list = map(float, temp_list)
		if len(temp_list)>0:
			rating = sum(temp_list)/len(temp_list)
			return rating
		temp_list = []


def make_lenskit_csv(rating_per_user):
	'''
	It will write the results into Mongodb
	Further we can export that file from mongodb inorder to use in lenskit
	'''
	for user in users:
		#print user
		userId = users.index(user) + 1
	 	for movie_id in random.sample(movie_id_list, rating_per_user):
	 		#print movie_id
	 		rate = movie_rating_calc(movie_id)
	 		#print rate
	 		if rate is not None:
	 			print userId,movie_id,rate
	 			# Writing the results into MongoDB
				#lenskit = db.lenskit.find()
				db.lenskit.insert_one({"userId":userId, "movieId":movie_id, "rating":rate})
	print "Results wrote into MongoDB"


if __name__ == "__main__":
	make_lenskit_csv(500)