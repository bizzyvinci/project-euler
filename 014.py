from math import floor

# This code is efficient because it saves every n that is solved in a dictionary
def count_chain(n):
	if n in values:
		return values[n]
	if n%2==0:
		values[n]=1+count_chain(n/2)
	else:
		values[n]=2+count_chain((3*n+1)/2)
	return values[n]
limit = 1000000
longest_chain = 0
answer = -1
values = {1:1}
for x in range(floor(limit/2), limit):
	if count_chain(x)>longest_chain:
		longest_chain=count_chain(x)
		answer=x
print(answer)
