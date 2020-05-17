from math import sqrt, floor, log

def collatz(n):
	if n<0: 
		return -1
	elif n==0:
		return 0
	elif n==1:
		return 1
	else:
		C=1
		while n!=1:
			if n%2==0:
				n=n/2  
			else: 
				n=(3*n+1)/2		# Take double steps
				C+=1
			C+=1
		return C
			


T=1000000
ls=[0 for i in range(0,T)]
# Set values for 0, 1 & 2
for i in range(0,3):
	ls[i]=i

# Set values for exponentials of 2
for i in range(1,int(floor(log(T,2)))):
	ls[2**(i+1)]=ls[2**i]+1

# Set values for odd numbers less than T/2
for i in range(3,(T//2)+1,2):
	C=collatz(i)
	ls[i]=C

# Set values for even numbers up to T
	j=2*i
	while j<T:
		C+=1
		ls[j]=C
		j*=2
		

# Set values for odd numbers greater than T/2
x=int(T//2)+1 if (T//2)%2==0 else int(T//2)+2 # Make sure to start from odd number
for i in range(x,T,2):
	ls[i]=collatz(i)

print(ls.index(max(ls)))

