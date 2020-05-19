from math import sqrt, floor, ceil

# The seive of eratothenes is used and only odd numbers are included in the list for sieving. Even numbers are already excluded.
limit = 2000000
sievebound=ceil((limit-1)/2)
sieve=[False for i in range(0,sievebound)]
crosslimit=ceil(floor(sqrt(limit)-1)/2)
for i in range(1,crosslimit):
	if not sieve[i]:
		for j in range(2*i*(i+1), sievebound, 2*i+1):
			sieve[j]=True
sum=2 	# 2 is the only even prime number
for i in range(1, sievebound):
	if not sieve[i]:
		sum+=2*i+1
print(sum)
