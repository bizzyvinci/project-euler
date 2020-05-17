

x,y=999,979 #y is a multiple of 11
roof=1
while x>990:
	while y>900:
		if str(x*y)==str(x*y)[::-1] and x*y>roof:
			roof=x*y
		y-=11
	y=979 # Reset y
	x-=1
print(roof)


#print(str(900*5)[::-1])
