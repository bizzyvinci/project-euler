'''
Solved by combination(m+n, n)
Which is equal to combination(m+n, m)
combination(a,b)=a!/((a-b)!b!)
The formula used below can be derived from the above formula. I don't know how to type it.
'''

def number_of_paths(m,n):
	up=1
	down=1
	for i in range(m+1, m+n+1):
		up*=i
	for j in range(1,n+1):
		down*=j
	return up/down

m=20
n=20
print(number_of_paths(m,n))