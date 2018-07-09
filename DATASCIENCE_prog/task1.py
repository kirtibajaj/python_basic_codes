import numpy as np
import math
l=[]
d={}
x=np.random.randint(1,100,100)
l=list(x)
class_no=1+3.322*math.log(100,10)
s=list(set(l))
size=round((max(s)-min(s))/class_no)
i=min(s)
j=min(s)+size
k=0
fx=[]
while k<class_no:
    c=0
    x=i
    while i<j:
        c=c+(l.count(i))
        i+=1
    d["{}-{}".format(int(x),int(j))]=c
    fx.append((x+((j-x)/2))*c)
    i,j=j,j+size
    k+=1
f=iter(fx)
print(x)
print("  Interval  ||  Frequency  ||  fx".center(100))
for i,j in d.items():
    print(("{}".format(i)).rjust(42),end="")
    print(("{}".format(j)).rjust(12),end="")
    print(("{}".format(next(f))).rjust(12))
print("Mean is : ",sum(fx)/100)
