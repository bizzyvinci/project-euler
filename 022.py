
value={'"':0, 'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 
		'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26
		}	# '"' was included to avoid KeyError: '"'
ans=0
names=open("022_names.txt", "r")
ls=sorted(names.read().split(","))			# I use sorted instead or sort() to make sure ls is a list
for i in range(len(ls)):
	alpha_value=0
	for char in ls[i]:
		alpha_value+=value[char]			# Workout alphabetical value
	score = alpha_value*(i+1)				# Multiply by alphabetical position in the list
	ans+=score

names.close()
print(ans)
