'''
Problem: What is the 10 001st prime number?
'''

from math import sqrt
def is_prime(x):
	y=3
	while y<=sqrt(x):
		if x%y==0: return False
		y+=2
	return True
C=2		# Count 2 and 3
x=3
while C<10001:
	x+=2	# Continue from 5 (odd numbers only)
	if is_prime(x): C+=1
print(x)	
