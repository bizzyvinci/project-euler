'''
Problem: Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

'''
I noticed that I have to ignore multiples of 2 and 5.
Then later I discovered that its best I work with primes only.
I don't know how to prove my point but I tested it with a few numbers.
For example the recurring_cycle of 7 and multiples of 7 is 6.

Ok. Probably not all multiples. I only tried a few with pen and paper.

Lastly, every recurring number can be represented by fraction with 9s as the denominator.
I didn't notice or discovered that. Wikipedia told me. Thanks Wiki

Right now, I'm so excited, so excited that I might not read what's on the forum or how it works.
I hope I do. But surely not now. I'm coming git
'''

from math import floor, sqrt, ceil

def list_primes(lim):
	# Seive of eratothenes
	# Very similar to 010.py
	# Note: 2 is excluded from this prime. We don't need it in this problem
	ans=[]
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

primal = list_primes(1000)
primal.pop(0)		# Remove 3. We don't need it
primal.pop(0)		# Remove 5. It is a big problem. _9_/5 can never resolve to whole number. We'll cycle endlessly in the while loop
highest = 0

for n in primal:
	c=0
	_9_=9
	while _9_%n!=0:
		c+=1
		_9_+=(9*10**c)
	recurring_cycle = len(str(_9_))
	if recurring_cycle>highest:
		highest = recurring_cycle
		ans = n
print(ans, highest)
