'''
Problem: What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''
x=1
ans=1
for i in range(2,1001,2):
	for j in range(4):
		x+=i
		ans+=x
print(ans)