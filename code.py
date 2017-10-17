
# from itertools import permutations
# perms = [''.join(p) for p in permutations('LLHLA')]



# print perms

# print(len(perms))


from itertools import permutations

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





k = k1+k2+k3+k4+k5+k6+k7+k8+k9+k11+k12+k13+k14+k15+k16+k17+k18+k19+k20+k21+k22
m = set(k)
final = []	
for i in m:
	final.append(i)

# print final       # Without sorting

if __name__ == "__main__":
	print 'USERS BASED ON PERSONALITY SCORES: "243" users'
	print sorted(final)
	print "TOTAL NUMBER OF USER TYPES:"+ str(len(final))











