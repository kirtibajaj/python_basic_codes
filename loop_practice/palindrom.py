num=int(input("Enter a number:"))
s=0
n=num
while(n):
	r=n%10
	s=s*10+r
	n=n//10
if s==num:
	print("Palindrom")
else:
	print("Not palindrom")
