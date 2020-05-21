'''
By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
'''

'''
even number appear at intervals of 3 from each other
b is the even number
fibonacci can be represented as a sequence of: a,b,a+b,a+2b,2a+3b
'''

a,b=1,2
even_sum=0

while b<4000000:
	even_sum+=b
	a,b=a+2*b, 2*a+3*b
print(even_sum)