'''
Note: this only works for odd numbers

'''
from math import sqrt
n=600851475143
d=3

while d<=sqrt(n):
	while n%d==0:
		n/=d
	d+=2
# The if statement is to avoid printing 1 when n is divided by sqrt(n)
print(n) if n!=1 else d-2