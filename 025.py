'''
Problem: What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

a,b = 1,1
t=2
target=1000

while len(str(b))!=target:
	a,b=b,a+b
	t+=1
print(t)