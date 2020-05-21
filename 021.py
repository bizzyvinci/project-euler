'''
Problem: Evaluate the sum of all the amicable numbers under 10000.
'''

from math import sqrt, ceil

def find_divisor_sum(num):
	x=ceil(sqrt(num))
	out=0
	for i in range(1, x):
		if num%i==0:
			out+=i+(num/i)
	if x*x==num:
		out+=x		# Add square root of num if it is an integer
	out-=num		# Remove num from the list of **PROPER** divisors
	return int(out)

N=10000
d={1:1, 2:1}
ans=0
for i in range(3,N):
	d[i]=find_divisor_sum(i)

for key,value in d.items():
	if value in d:
		if key==d[value] and key!=value:
			ans+=key
print(ans)