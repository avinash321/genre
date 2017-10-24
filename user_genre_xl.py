'''
It will take the input as  a personality code and 
returns a list of generes recommended for that personality code

Source : This caliculatons are made based on Empoire Docujment
http://ceur-ws.org/Vol-997/empire2013_paper_2.pdf
'''
from user_codes import users
import xlsxwriter

# This are list of genres from Empire Document
genres = ["action", "adventure", "animation", "cartoon", "comedy", "cult", "drama", "foreign", "horror", 
            "independent", "neo-noir", "parody", "romance", "science fiction", "tragedy", "war"]

# These ratings are respective with the abvove mentioned genres
ope = [3.87, 3.91, 4.04, 3.95, 3.88, 4.27, 3.99, 4.15, 3.90, 4.31, 4.34, 4.13, 3.84, 3.99, 4.40, 3.82]

con = [3.45, 3.56, 3.22, 3.33, 3.44, 3.10, 3.43, 3.46, 3.38, 3.59, 3.35, 3.36, 3.48, 3.55, 3.34, 3.51]

ext = [3.57 ,3.54 ,3.26 ,3.49 ,3.58 ,3.45 ,3.66 ,3.47 ,3.52 ,3.51 ,3.33 ,3.35 ,3.62 ,3.33 ,3.27 ,3.49 ]

agr = [3.58, 3.68, 3.35,3.57, 3.60, 3.40, 3.60, 3.54, 3.47, 3.55, 3.37, 3.28, 3.62, 3.57, 3.52, 3.50]

nur = [2.72, 2.61, 3.02, 2.81, 2.75, 3.16, 2.86, 2.81, 2.91, 2.69, 2.97, 2.73, 2.85, 2.73, 3.11, 2.71]

def genre_calc(persona_code, persona_list): 
    '''
    parameters:
        persona_list:  list of ratings for the concerned personality type (ex: ope list)
        persona_code:  A single char from the complete user personality 
        (ex: user personality - HAALL  &  single char - H )
    Description:
        It will seperates the given personality list into High, Low and average based on avg value
        Note: High = > avg+0.10 , Low = > avg-0.10 and remainings are Avg
        It will returns the list of genres for the 
    Returns:
        It will returns the list of genres for the given persona list based on persona_code( H | L | A)
    '''
    persona_list_high = []
    persona_list_avg = []
    persona_list_low = []
    persona_avg= sum(persona_list)/len(persona_list)        # Caliculating Average
    #Preparing 3 different lists from the persona list (i.e: High, Low & Avg)
    for idx, score in enumerate(persona_list):
        if score > persona_avg + 0.10:
            score_index = idx
            genre = genres[score_index]
            persona_list_high.append(str(score) + "," + genre)
        elif score < persona_avg - 0.10:
            score_index = idx
            genre = genres[score_index]
            persona_list_low.append(str(score) + ',' + genre)
        else:
            score_index = idx
            genre = genres[score_index]
            persona_list_avg.append(str(score) + ',' + genre)

    if persona_code == "H":
        return persona_list_high
    elif persona_code == "A":
        #return em_list
        return persona_list_avg
    elif persona_code == "L":
        #return em_list
        return persona_list_low

def avg_genre(genre_list):
    '''
    parameters:
        genre_list: It will take the list of genres
    Returns:
        It will returns the average genre from the given list based on rating
    '''
    full_list = []
    for i in genre_list:
        full_list = full_list + i.split(",")            
    myrating,mygenre = full_list[::2], full_list[1::2]
    myrating = map(float , myrating)
    avg_number = sum(myrating) / len(myrating)
    # caliculating the genre rating that is nearer to the Average number
    result_num = min(myrating, key=lambda x:abs(x-avg_number))
    result_index = myrating.index(result_num)
    avg_genre = genre_list[result_index]
    return avg_genre

def get_duplicate_index(mygenre_list, genre):
    # It will Returns the Duplicate items Index values in a list for the given list
     return filter(lambda a: mygenre_list[a]==genre, range(0,len(mygenre_list)))

def remove_duplicates(genres_list):
    '''
    Parameters:
        It will take the input as a list of genres
    Description:
        In the given list if any duplicate genres are found, then it will caliculates
        the average of those duplicate genre ratings & 
        then returns single genre with theaverage value as rating.
    Return:
        It will returns the given list by removing duplicate items
    '''
    top5_genre = []
    full_list = []
    # Generating  myrating,mygenre lists from the full_list
    for i in genres_list:
        full_list = full_list + i.split(",")
    myrating,mygenre = full_list[::2], full_list[1::2]
    # mylist will store the duplicate Indexes in a list format for every item (ex:[0,3])
    mylist = []
    for genre in mygenre:
        mylist.append(get_duplicate_index(mygenre, genre))
    # rate_list will stores the average rating for each genre in the list
    rate_list = []
    for sub_list in mylist:
        new_list = []
        for rate in sub_list:
            new_list.append(myrating[rate])
        new_list = map(float , new_list)
        avg=sum(new_list)/len(new_list)
        rate_list.append(avg)
        new_list = []
    #Removing Duplicares by applyintg set
    for i in zip(rate_list,mygenre):
        top5_genre.append(str(i[0]) + "," + i[1])
    top5_genre = list(set(top5_genre))
    return top5_genre


def top5_user_genre(user_code):
    '''
    parameters:
        user_code: It is personality code for the user  (ex: LAAHA)
    Description:
        On the basis of user_code , for every character in the user_code ,
        It will invokes the genre_calc method & returns respective genres list.
    Returns:
        It will returns the top5 genres for the given user_code.
    '''
    top5_genre = []
    persona_code = user_code       
    #ex:  "LLHAA"  ---->   EACNO
    # Caliculation logic is written by considering (EACNO - HHAAL)
    personality = [ext, agr, con, nur, ope]
    aggr = zip(persona_code,personality)
    for i in range(len(persona_code)):
      mycode = aggr[i][0]
      mypersona_list = aggr[i][1]
      mygenre_list = genre_calc(mycode, mypersona_list)
      '''
      Logic:
        From the Resulted list, 
        --> If the code is "H" ,  we will take the max vlue (genre) from the list
        --> If the code is "L" ,  we will take the min value (genre) from the list
        --> And If the code is "A"  we will take the average (genre) from the list
      '''

      if mycode == 'H':
        val = max(mygenre_list)
        top5_genre.append(val)

      if mycode == 'A':
        val = avg_genre(mygenre_list)
        top5_genre.append(val)

      if mycode == 'L':
        val = min(mygenre_list)
        top5_genre.append(val)
    # Removing Duplicate Items
    top5_genre = remove_duplicates(top5_genre)  
    # Sorting the genres from Highier to lower based on rating    
    top5_genre = sorted(top5_genre, reverse=True)
    return top5_genre


def get_user_genres_xl(path):
    #preparing genres for respective user types
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()
    user_type = users
    for user in user_type:
        genre_list = top5_user_genre(user)
        user_genre = "|".join(genre_list)
        worksheet.write('A'+str(user_type.index(user)+1), user)
        worksheet.write('B'+str(user_type.index(user)+1), user_genre)
    workbook.close()


if __name__ == "__main__":
    get_user_genres_xl('/home/py01/Desktop/user_genre.xlsx')
    print "User_Genre Xl Sheet Generated Successfully"
    #mygenre = top5_user_genre("LLLHA")
    #print mygenre














    # persona_code = "A"
    # print "Openness"
    # print genre_calc(persona_code, ope)
    # print "Consoentiouness"
    # print genre_calc(persona_code, con)
    # print "Extroversion"
    # print genre_calc(persona_code, ext)
    # print "Agreeableness"
    # print genre_calc(persona_code, agr)
    # print "nurotisicisum"
    # print genre_calc(persona_code, nur)


    #   final_list = final_list + k

    # u_list = set(final_list)
    # result = []
    # for i in u_list:
    #     result.append(i)
    # return result



#preparing genres for respective user types
# workbook = xlsxwriter.Workbook('/home/py01/Desktop/hello.xlsx')
# worksheet = workbook.add_worksheet()
# user_type = code.final
# for i in user_type:
#     k1 = get_genre(i)
#     k2 = "|".join(k1)
#     print k2
#     worksheet.write('A'+str(user_type.index(i)+1), k2)
# workbook.close()



#Preparing an excel Sheet with user types along with those genre types
# user_type = code.final
# workbook = xlsxw
#riter.Workbook('/home/py01/Desktop/hello.xlsx')
# worksheet = workbook.add_worksheet()
# for i in user_type:
#     worksheet.write('A'+str(user_type.index(i)+1), i)

# workbook.close()



# Duplicate Logic
    # D = defaultdict(list)
    # for i,item in enumerate(mygenre):
    #     D[item].append(i)
    # D = {k:v for k,v in D.items() if len(v)>1}
    # mykeys = D.keys()
    # print "these are keys"
    # print D.keys()
    # myvalues  = D.values()
    # mylist = []
    # mylist2 = []
    # for i in zip(myrating,mygenre):
    #     #print i[1]
    #     if i[1] not in mykeys:
    #         top5_genre.append(i[0] + "," + i[1])

    #     elif i[1] in mykeys:
    #         if i[1] not in mylist2:
    #             mylist.append(i[0] + "," + i[1])
    #             mylist2.append(i[1])
    #             #print i[0]
    # if mylist:
    #     print "This is mylist"
    #     print mylist
    #     #mylist = map(float , mylist)
    #     #myavg = sum(mylist)/len(mylist)
    #     #top5_genre.append(str(myavg) + "," + mykeys[0])