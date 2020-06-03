'''
Problem: Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
ans=0
ls=[]
for i in range(4000,354295):		# It cannot exceed 6 digits and 6*(9**5)=354294. After running the code the lowest was 4150
	num=i
	sum_of_powers=0
	while num!=0:
		d=num%10
		num//=10
		sum_of_powers+=d**5
	if sum_of_powers==i:
		ans+=i
		ls.append(i)
print(ans,ls)