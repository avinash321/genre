'''
It will take the input as  a personality code and 
returns a list of generes recommended for that personality code.import 
'''
import code
import xlsxwriter


'''
# This are list of genres from Empire Document
genres = ["action", "adventure", "animation", "cartoon", "comedy", "cult", "drama", "foreign", "horror", 
            "independent", "neo-noir", "parody", "romance", "science fiction", "tragedy", "war"]
'''
# This are modified genres based on IMDB
genres = ["Action", "Adventure", "Animation", "Children", "Comedy", "Documentary", "Drama", "Western", "Horror", 
            "Fantasy", "Film-Noir", "Musical", "Romance", "Sci-Fi", "Mystery", "War","Crime","Thriller"]
ope = [3.87, 3.91, 4.04, 3.95, 3.88, 4.27, 3.99, 4.15, 3.90, 4.31, 4.34, 3.84, 3.84, 3.99, 4.40, 3.82, 3.87, 3.91 ]
ope_avg  = sum(ope)/len(ope)

con = [3.45, 3.56, 3.22, 3.33, 3.44, 3.10, 3.43, 3.46, 3.38, 3.59, 3.35, 3.48, 3.48, 3.55, 3.34, 3.51, 3.45, 3.56]
con_avg = sum(con)/len(con)

ext = [3.57 ,3.54 ,3.26 ,3.49 ,3.58 ,3.45 ,3.66 ,3.47 ,3.52 ,3.51 ,3.33 ,3.62 ,3.62 ,3.33 ,3.27 ,3.49, 3.57, 3.54]
ext_avg  = sum(ext)/len(ext)

agr = [3.58, 3.68, 3.35,3.57, 3.60, 3.40, 3.60, 3.54, 3.47, 3.55, 3.37, 3.62, 3.62, 3.57, 3.52, 3.50, 3.58, 3.68]
agr_avg = sum(agr)/len(agr)

nur = [2.72, 2.61, 3.02, 2.81, 2.75, 3.16, 2.86, 2.81, 2.91, 2.69, 2.97, 2.85, 2.85, 2.73, 3.11, 2.71, 2.72,2.61]
nur_avg = sum(nur)/len(nur)


#print ope_avg, con_avg, ext_avg, agr_avg, nur_avg

def genre_calc(persona, avg, code):
    persona_list_high = []
    persona_list_avg = []
    persona_list_low = []
    for idx, score in enumerate(persona):
        if score > avg + 0.10:
            score_index = idx
            genre = genres[score_index]
            #persona_list_high.append(genre)
            #persona_list_high.append(genre +','+str(score))
            persona_list_high.append(str(score) + "," + genre)
        elif score < avg - 0.10:
            score_index = idx
            genre = genres[score_index]
            #persona_list_low.append(genre)
            #persona_list_low.append(genre + ','+str(score))
            persona_list_low.append(str(score) + ',' + genre)
        else:
            score_index = idx
            genre = genres[score_index]
            #persona_list_avg.append(genre)
            #persona_list_avg.append(genre + ','+str(score))
            persona_list_avg.append(str(score) + ',' + genre)
    em_list = []
    if code == "H":
        return persona_list_high
    elif code == "A":
        #return em_list
        return persona_list_avg
    elif code == "L":
        #return em_list
        return persona_list_low


def find_avg(in_list):
    full_list = []
    for i in in_list:
        full_list = full_list + i.split(",")

    myscore,mygenre = full_list[::2], full_list[1::2]
    myscore = map(float , myscore)
    mynumber = sum(myscore) / len(myscore)
    result_num = min(myscore, key=lambda x:abs(x-mynumber))
    result = myscore.index(result_num)
    avg_genre = mygenre[result]
    avg_genre = str(result_num) + ',' + avg_genre
    return avg_genre

    #print persona_list_high
    #print persona_list_avg
    #print persona_list_low
# persona_code = "H"

# print "Openness"
# print genre_calc(ope, ope_avg, persona_code)
# print "Consoentiouness"
# print genre_calc(con, con_avg, persona_code)
# print "Extroversion"
# print genre_calc(ext, ext_avg, persona_code)
# print "Agreeableness"
# print genre_calc(agr, agr_avg, persona_code)
# print "nurotisicisum"
# print genre_calc(nur, nur_avg, persona_code)


def list_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [idx for idx,item in enumerate(seq) if item in seen or seen_add(item)]

def get_genre(code):

    persona_code = code      #ex:  "LLHAA"    # EACNO
    personality = [ext, agr, con, nur, ope]
    personality_avg = [ext_avg, agr_avg, con_avg, nur_avg, ope_avg]

    aggr = zip(persona_code,personality,personality_avg)
    # for i in aggr:
    #     print aggr
      #print genre_calc(ope, ope_avg, code)

    #final_list = []
    top5_genre = []
    for i in range(len(persona_code)):
      mycode = aggr[i][0]
      mypersona = aggr[i][1]
      mypersona_avg = aggr[i][2]
      k = genre_calc(mypersona, mypersona_avg, mycode)
      print k
      # Here iam getting the list of genres based on single code
      if mycode == 'H':
        val = max(k)
        #val = val.split(",")
        #val = val[1]
        top5_genre.append(val)

      if mycode == 'A':
        val = find_avg(k)
        top5_genre.append(val)
      if mycode == 'L':
        val = min(k)
        #val = val.split(",")
        #val = val[1]
        top5_genre.append(val)

    top5_genre = list(set(top5_genre))

    # # Small logic to remove duplicates
    # final_genre = []
    # l =[]
    # for i in top5_genre:
    #     l = l + i.split(",")
    # print l 
    # l1 = l[::2]
    # l2 = l[1::2]
    # print l1
    # print l2
        
    # print list_duplicates(l2)

    return top5_genre




# TESTING
if __name__ == "__main__":
    k = get_genre("HAHAL")
    print k

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

