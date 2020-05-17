import math
# a+b+c=1000 && a^2+b^2==c^2
for a in range(1,335):
	found=False
	b=math.floor((1000-a)/2)
	c=math.ceil((1000-a)/2)
	while a**2+b**2>c**2:
		b-=1
		c+=1
		if a**2+b**2==c**2:
			# Solution and output
			print(a*b*c)
			found=True
			break
	# Break out of for loop
	if found:
		break