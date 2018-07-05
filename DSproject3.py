from random import randint
import math
n=int(input("Enter no of observation : "))
print("Enter no for this observation separated by ,")
l=list(map(int,input().split(",")))
l1=list(set(l))
l1.sort()
item=[]
length=len(l1)
class_interval=round(1+3.322*math.log(n,10))
maximum=max(l1)
minimum=min(l1)
size=round((maximum-minimum)/class_interval)
print("\n\n\n\n")
print("Number    : frequency :  fx ".center(145))
c=0
i=minimum
j=minimum+size
k=0
while k<class_interval:
    c=0
    x=i
    fx=0
    while i<j:
        c=c+(l.count(i))
        i+=1
        fx+=i*j
    item.append(("{}-{}".format(x,j)))
    item.append(c)
    item.append(fx)
    i,j=j,j+size
    k+=1
for i,j,k in item:
    print(("{}".format(i)).rjust(60),end="")
    print(("{}".format(j)).rjust(12),end="")
    print(("{}".format(k)).rjust(8))
print(l)
