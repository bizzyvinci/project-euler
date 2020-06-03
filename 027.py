'''
Problem: Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0
Considering quadratics of the form:
	n^2+an+b, where |a|<1000 and |b|≤1000
'''

'''
It's too damn slow
'''


from math import sqrt, floor, ceil

def list_primes(lim):
	# Seive of eratothenes
	# Very similar to 010.py
	ans=[2]
	sievebound=ceil(lim/2)-1		# total odd numbers is ceil() while total even numbers is floor().
	sieve=[False]*sievebound		# -1 because index starts from 0
	crosslimit=floor((sqrt(lim)-1)/2)
	for i in range(crosslimit):	# No need for +1 because of -1 (instead of -3 above)
		if not sieve[i]:
			for j in range(2*i*(i+3)+3, sievebound, 2*i+3):
				sieve[j]=True
	for i in range(sievebound):
		if not sieve[i]:
			ans.append(2*i+3)
	return ans

primes = list_primes(100000)
highest=0
a_max=999
b_max=1000
for a in range(-a_max, a_max+1, 2):		############## ,2
	for b in primes:
		if b>b_max:
			break
		else:
			n = 0
			eq = n*n+a*n+b
			while eq in primes:
				n+=1
				eq = n*n+a*n+b
			if n>highest:
				ans=a*b
				highest=n
				aa=a
				bb=b
print(ans, aa, bb, highest)

