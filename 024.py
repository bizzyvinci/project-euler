'''
Problem: What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

from math import factorial
N=1000000
digits=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ans=""
destination=0

for i in range(len(digits)-1,0,-1):		# 9 to 1
	index=0
	while destination+factorial(i)<N:	# I used less than because we're starting the arrangement from 0 (not 1)
		destination+=factorial(i)
		index+=1
	ans+=digits.pop(index)
ans+=digits.pop(0)						# Had to be excluded from the loop because factorial(0)==factorial(1)==1
print(ans)
