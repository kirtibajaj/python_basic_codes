from random import randint
import math
l=[]
n=int(input("Enter number of observation"))
for i in range(n):
    l.append(randint(1,100))
l1=list(set(l))
l1.sort()
length=len(l1)
class_interval=round(1+3.322*math.log(n,10))
size=round((max(l1)-min(l1))/class_interval)
d={}
print("\n\n\n\n")
fx=0
f=0
for i in l1:
    d[i]=l.count(i)
    fx+=i*(l.count(i))
    f+=l.count(i)
    
print("Number    : frequency".center(145))
c=0
i=min(l1)
j=min(l1)+size
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
print(fx/f)
