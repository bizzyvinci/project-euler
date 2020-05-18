
ans=0
# zero, one, two, three, four, five, six, seven, eight, nine
zero=[0,3,3,5,4,4,3,5,5,4]

# ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen
ten=[3,6,6,8,8,7,7,9,8,8]

# twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety
tens=[6,6,5,5,5,7,6,6]



for i in range(0,10):
	ans+=zero[i]				#zeroes
	ans+=ten[i]					#ten
	for j in range(0,8):		#tens
		ans+=tens[j]+zero[i]

	# Repeat myself for 100-999
	for j in range(1,10):		#hundreds
		ans+=zero[j]+10+zero[i]	#7+3(hundred+and)
		ans+=zero[j]+10+ten[i]
		for k in range(0,8):
			ans+=zero[j]+10+tens[k]+zero[i]

ans-=(3*9)						# *hundred was counted as *hundred-and for 100,200, ... 900
ans+=3+8						#Last but not the least ONE THOUSAND

print(ans)