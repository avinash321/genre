'''
It will take the input as  a personality code and 
returns a list of generes recommended for that personality code.import 
'''

genres = ["action", "adventure", "animation", "cartoon", "comedy", "cult", "drama", "foreign", "horror", 
            "independent", "neo-noir", "parody", "romance", "science fiction", "tragedy", "war"]

ope = [3.87, 3.91, 4.04, 3.95, 3.88, 4.27, 3.99, 4.15, 3.90, 4.31, 4.34, 4.13, 3.84, 3.99, 4.40, 3.82]
ope_avg  = sum(ope)/len(ope)

con = [3.45, 3.56, 3.22, 3.33, 3.44, 3.10, 3.43, 3.46, 3.38, 3.59, 3.35, 3.36, 3.48, 3.55, 3.34, 3.51]
con_avg = sum(con)/len(con)

ext = [3.57 ,3.54 ,3.26 ,3.49 ,3.58 ,3.45 ,3.66 ,3.47 ,3.52 ,3.51 ,3.33 ,3.35 ,3.62 ,3.33 ,3.27 ,3.49 ]
ext_avg  = sum(ext)/len(ext)

agr = [3.58, 3.68, 3.35,3.57, 3.60, 3.40, 3.60, 3.54, 3.47, 3.55, 3.37, 3.28, 3.62, 3.57, 3.52, 3.50]
agr_avg = sum(agr)/len(agr)

nur = [2.72, 2.61, 3.02, 2.81, 2.75, 3.16, 2.86, 2.81, 2.91, 2.69, 2.97, 2.73, 2.85, 2.73, 3.11, 2.71]
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
            persona_list_high.append(genre)
        elif score < avg - 0.10:
            score_index = idx
            genre = genres[score_index]
            persona_list_low.append(genre)
        else:
            score_index = idx
            genre = genres[score_index]
            persona_list_avg.append(genre)
    em_list = []
    if code == "H":
        return persona_list_high
    elif code == "A":
        #return em_list
        return persona_list_avg
    elif code == "L":
        #return em_list
        return persona_list_low

    #print persona_list_high
    #print persona_list_avg
    #print persona_list_low
persona_code = "H"

print "Openness"
print genre_calc(ope, ope_avg, persona_code)
print "Consoentiouness"
print genre_calc(con, con_avg, persona_code)
print "Extroversion"
print genre_calc(ext, ext_avg, persona_code)
print "Agreeableness"
print genre_calc(agr, agr_avg, persona_code)
print "nurotisicisum"
print genre_calc(nur, nur_avg, persona_code)




# persona_code = "AAHLL"    # EACNO
# personality = [ext, agr, con, nur, ope]
# personality_avg = [ext_avg, agr_avg, con_avg, nur_avg, ope_avg]

# aggr = zip(persona_code,personality,personality_avg)
# # for i in aggr:
# #     print aggr
#   #print genre_calc(ope, ope_avg, code)

# final_list = []
# for i in range(len(persona_code)):
#   mycode = aggr[i][0]
#   mypersona = aggr[i][1]
#   mypersona_avg = aggr[i][2]
#   k = genre_calc(mypersona, mypersona_avg, mycode)
#   final_list = final_list + k

# m = set(final_list)
# print m
# print(len(m))



