'''
This will generate the 243 Users in a list,  based on different set of 
permutations of the personality types. {OCEAN} (ex: HAHAL)
'''
from itertools import permutations
# Caliculating Permutations
k1 = [''.join(p) for p in permutations('LLLLL')]

k2 = [''.join(p) for p in permutations('AAAAA')]

k3 = [''.join(p) for p in permutations('HHHHH')]
k4 = [''.join(p) for p in permutations('LLLLA')]
k5 = [''.join(p) for p in permutations('LLLAA')]

k6 = [''.join(p) for p in permutations('LLAAA')]

k7 = [''.join(p) for p in permutations('LAAAA')]

k8 = [''.join(p) for p in permutations('LLLLH')]

k9 = [''.join(p) for p in permutations('LLLHH')]

k11 = [''.join(p) for p in permutations('LLHHH')]
k12 = [''.join(p) for p in permutations('LHHHH')]

k13 = [''.join(p) for p in permutations('HHHHA')]
k14 = [''.join(p) for p in permutations('HHHAA')]
k15 = [''.join(p) for p in permutations('HHAAA')]
k16 = [''.join(p) for p in permutations('HAAAA')]

k17 = [''.join(p) for p in permutations('LAHLL')]
k18 = [''.join(p) for p in permutations('LAHHH')]
k19 = [''.join(p) for p in permutations('LAHAA')]

k20 = [''.join(p) for p in permutations('LAHLA')]
k21 = [''.join(p) for p in permutations('LAHLH')]
k22 = [''.join(p) for p in permutations('LAHAH')]

total_permutations = k1+k2+k3+k4+k5+k6+k7+k8+k9+k11+k12+k13+k14+k15+k16+k17+k18+k19+k20+k21+k22
# Removing Duplicate permutations
user_codes = set(total_permutations)
users = []	
for code in user_codes:
	users.append(code)

if __name__ == "__main__":
	print 'USERS BASED ON PERSONALITY SCORES: "243" users'
	print sorted(users)
	print "TOTAL NUMBER OF USER TYPES:"+ str(len(users))











