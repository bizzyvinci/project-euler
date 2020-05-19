N= [75,
	[95,64],
	[17,47,82],
	[18,35,87,10],
	[20,4,82,47,65],
	[19,1,23,75,3,34],
	[88,2,77,73,7,63,67],
	[99,65,4,28,6,16,70,92],
	[41,41,26,56,83,40,80,70,33],
	[41,48,72,33,47,32,37,16,94,29],
	[53,71,44,65,25,43,91,52,97,51,14],
	[70,11,33,28,77,73,17,78,39,68,17,57],
	[91,71,52,38,17,14,91,43,58,50,27,29,48],
	[63,66,4,68,89,53,67,30,73,16,69,87,40,31],
	[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
]


rows=15
# new and previous are list of a list=[index, sum_from_top]
new=[]
previous=[[0,N[0]]]
for i in range(rows-1):
	for j in range(2**i):
		index=previous[j][0]
		num=previous[j][1]
		add1 = num+N[i+1][index]
		add2 = num+N[i+1][index+1]
		new.append([index,add1])
		new.append([index+1,add2])
	previous=new
	new=[]
highest_num = max(previous, key=lambda x: x[1])
print(highest_num[1])


# Wasting my time not trying to bruteforce and asking my self if
# I'll probably get back but the bruteforce if fast enough (so I might not)
'''
n=0
ans=N[n]


def eliminate(m,n):					# Eliminate one of the extreme paths
	add1=0
	add2=0
	for i in range(1,rows-m):
		add1+=N[m+i][n]
		add2+=N[m+i][n+i]
	if add1>add2:
		return 1
	elif add1<add2:
		return 2
	else:
		return 0

for m in range(rows-1):				# Exclude the last row
	if eliminate(m,n):
		if eliminate(m,n)==1:
			if N[m+1][n] >= N[m+1][n+1]:
				ans+=N[m+1][n]
				n+=0
			else:
				print("I'm screwed")
				# I'm coming for the else statement
		else:
			ans+=N[m+1][n+1]
			n+=1
	else:
		if N[m+1][n] > N[m+1][n+1]:
			ans+=N[m+1][n]
			n+=0
				# I'm coming for the else statement
		elif N[m+1][n] < N[m+1][n+1]:
			ans+=N[m+1][n+1]
			n+=1
		else:
			print("Yip! Yip! I'm indeed screwed")
print(ans)
'''