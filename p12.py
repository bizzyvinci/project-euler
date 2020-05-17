''' 
NOTE:
1. n and n+1 are co-prime (they don't have common prime numbers)
2. d(n)=(a+1)*(b+1)*....*(z+1)
	where a, b...z are exponentials of the unique prime factors in n
	and d(n) is the number of divisors of n
3. Because of #1 d(n*n1/2)=d(n/2)*d(n1)   (when n is even else d(n)*d(n1/2))
	where n1=n+1
4. This one was very hard for me :)
'''


primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,
103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,
199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,
313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,
433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,
563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,
673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,
811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,
941,947,953,967,971,977,983,991,997]
# Alternatively, use seive of eratothenes to generate the primes (as shown in p10)
# primes < 1000 is a safe bound for this problem

n=12373		# Start with a prime. Good place to start is 3, but I already that n=12376
Dn=2	# number of divisors for any prime
C=0

while C<=500:
	n=n+1
	n1=n
	if n1%2==0: n1=n1/2
	# Solve for Dn1, Dn would be inherited from the assignment (above) or previous while loop (below)
	Dn1=1
	for p in primes:
		if p*p>n1:
			Dn1=2*Dn1
			break
		exponent=1
		while n1%p==0:
			exponent+=1
			n1/=p
		if exponent>1: Dn1*=exponent
		if n1==1: break
	C=Dn*Dn1
	Dn=Dn1
print(n*(n-1)/2)

