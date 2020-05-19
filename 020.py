f=1
ans=0
for num in range(1,101):
	f*=num
s=str(f)
for digit in s:
	ans+=int(digit)
print(ans)