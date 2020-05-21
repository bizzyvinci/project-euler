'''
Problem: Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers
'''

from math import sqrt, ceil

sufficient=[]
N=28123
is_true={}
ans=0

def find_divisor_sum(num):
	# Find the sum of **PROPER** divisors of num
	x=ceil(sqrt(num))
	out=0
	for i in range(1, x):
		if num%i==0:
			out+=i+(num/i)
	if x*x==num:
		out+=x		# Add square root of num if it is an integer
	out-=num		# Remove num from the list of **PROPER** divisors
	return int(out)

def is_abundant(num):
	# Check if num is abundant
	return True if num<find_divisor_sum(num) else False

for i in range(12,N+1):
	# Make a list of all abundant numbers between 12 and 
	if is_abundant(i):
		sufficient.append(i) 

for i in range(1, N+1):
	# Preset all value to false
	is_true[i]=False

x=len(sufficient)
for i in range(x):
	for j in range(i, x+1):
		# Add all possible combination of sufficient and set the value to True
		y=sufficient[i]+sufficient[j]
		if y in is_true:
			is_true[y] = True
		else:
			break

for key, value in is_true.items():
	if value==False:
		ans+=key 

print(ans)


