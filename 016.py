'''
Problem: What is the sum of the digits of the number 21000?
'''

digits=str(2**1000)
s=0

for i in digits:
	s+=int(i)
print(s)