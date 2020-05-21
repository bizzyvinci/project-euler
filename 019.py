'''
Problem: How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

month=[31,28,31,30,31,30,31,31,30,31,30,31]
day_sum=0
C=0
for i in range(25):
	month[1]=28			#reset February
	for m in range(12):
		for j in range(3):
			day_sum+=month[m]
			if day_sum%7==6:
				C+=1
		month[1]=29		# leap year
		day_sum+=month[m]
		if day_sum%7==6:
			C+=1
if day_sum%7==6:
	C-=1				# Check and act if Jan 1 2001 is Sunday
print(C)