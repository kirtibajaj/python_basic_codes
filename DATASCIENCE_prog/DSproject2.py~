from random import randint
import math
l=[]
n=int(input("Enter no of observation : "))
for i in range(n):
    l.append(randint(1,100))
l1=list(set(l))
l1.sort()
d={}
length=len(l1)
class_interval=round(1+3.322*math.log(n,10))
maximum=max(l1)
minimum=min(l1)
size=round((maximum-minimum)/class_interval)
print("\n\n\n\n")
print("Number    : frequency".center(145))
c=0
i=minimum
j=minimum+size
k=0
while k<class_interval:
    c=0
    x=i
    while i<j:
        c=c+(l.count(i))
        i+=1
    d["{}-{}".format(x,j)]=c
    i,j=j,j+size
    k+=1
for i,j in d.items():
    print(("{}".format(i)).rjust(67),end="")
    print(("{}".format(j)).rjust(12))
print(l)
