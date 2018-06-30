import math
n=int(input("Enter a number to find krishna murti number:"))
num=n
s=0
while n!=0:
    r=n%10
    n=n//10
    s+=math.factorial(r)
if s==num:
    print("Krishnan murti number")
else:
    print("Not krishnan murti number")
x=int(input("Starting from range:"))
y=int(input("Ending at range:"))
for i in range(x,y+1):
    num=i
    s=0
    while num!=0:
        r=num%10
        num=num//10
        s+=math.factorial(r)
    if s==i:
        print(s,end="\t")

