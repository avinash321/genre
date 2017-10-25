'''
This will generate the CSV File with the columns "userId", "movieId", and "rating" (In MongoDB)
We can use/replace this File directly in lenskit recommendation Engine.
Based on this we can recommend top 10 recommndations of a respective user(type)
'''
from pymongo import MongoClient
import genre
import random
from user_codes import users
from user_genre_xl import top5_user_genre, get_csv_from_excel
import xlsxwriter
import xlrd
import csv
from multiprocessing import Pool
from multiprocessing import Process,Manager


#Connecting Mongo DB
client = MongoClient('localhost', 27017)
db = client.genre           #Getting Database (genre)

# It will write user_genres into mongodb in user_genres collection
for user in users:
    genre_list = top5_user_genre(user)
    user_genre = "|".join(genre_list)
    db.user_genres.insert_one({"userId":user, "genres":user_genre })

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


def movie_rating_calc(movie_id, return_dict):
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
    client = MongoClient('localhost', 27017)
    db1 = client.genre           #Getting Database (genre)
    imdb_movieId_cursor = db1.imdb_genres.find( {"movieId":movie_id } )
    imdb_genre = None
    for cursor_obj in imdb_movieId_cursor:
        imdb_genre =  cursor_obj["genres"]
    # This is the genre of the given movieId 
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
          return_dict[movie_id] = rating,movie_id
          #return rating
        temp_list = []


def make_lenskit_csv(path, rating_per_user):
    '''
    It will write the results into Mongodb
    Further we can export that file from mongodb inorder to use in lenskit
    '''
    print "Preparing User_rating document ..."
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', "userId")
    worksheet.write('B1', "movieId")
    worksheet.write('C1', "rating")

    count = 2
    for user in users:
      userId = users.index(user) + 1
      manager = Manager()
      return_dict = manager.dict()
      jobs = []
      for movie_id in random.sample(movie_id_list, rating_per_user):
        p = Process(target=movie_rating_calc, args=(movie_id,return_dict))
        jobs.append(p)
        p.start()
      for proc in jobs:
        proc.join()
      print return_dict.values()

          #rate = movie_rating_calc(movie_id)
    #       if rate is not None:
    #           print userId,movie_id,rate
    #           worksheet.write('A'+str(count), userId)
    #           worksheet.write('B'+str(count), movie_id)
    #           worksheet.write('C'+str(count), rate)
    #           count += 1
    #           # Writing the results into MongoDB
    #           #lenskit = db.lenskit.find()
    #           #db.lenskit.insert_one({"userId":userId, "movieId":movie_id, "rating":rate})
    # workbook.close()
    # get_csv_from_excel(path)
    # print "ratings.csv file generated successfully on Desktop"

def get_user_rating_xl(path):
    ''''
        It will prepares an excelsheet of  genres for respective user types
    '''
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', "userId")
    worksheet.write('B1', "genres")
    user_type = users
    for user in user_type:
        genre_list = top5_user_genre(user)
        user_genre = "|".join(genre_list)
        worksheet.write('A'+str(user_type.index(user)+2), user)
        worksheet.write('B'+str(user_type.index(user)+2), user_genre)
    workbook.close()


def clean_data():
    db.user_genres.delete_many({})
    
if __name__ == "__main__":
    ratings_per_user = 501
    path = '/home/py01/Desktop/ratings' + str(ratings_per_user)+'.csv'
    make_lenskit_csv(path ,ratings_per_user)
    clean_data()
