num=int(input("Enter a number:"))
s=0
n=num
x=0
while(n):
    n=n//10
    x+=1
n=num
while(n):
	r=n%10
	s=s+pow(r,x)
	n=n//10
if s==num:
	print("Armstrong")
else:
	print("Not Armstrong")


#To find in range of python:
a=int(input("Enter the start of number from where we have to print armstrong:"))
z=int(input("Enter end of numbers:"))
for i in range(a,z+1):
    n=i
    s=0
    x=0
    while(n):
        n=n//10
        x+=1
    n=i
    while(n):
        r=n%10
        s=s+pow(r,x)
        n=n//10
    if s==i:
        print(i,end="\t")
