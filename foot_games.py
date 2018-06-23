from random import randint
import math
step=randint(0,10)
l=[]
step1=[0,0]
print("Computer chooses to step {} points:".format(step))
for i in range(step):
    x=int(input("Enter x  of {}step:".format(i+1)))
    y=int(input("Enter y  of {}step:".format(i+1)))
    step1=[x,y]
    l.append(step1)
sx=0
sy=0
for i in range(step):
    sx+=l[i][0]
    sy+=l[i][1]
print("Total distance from house as origin:",sx+sy,"m")
d=math.sqrt(sx*sx+sy*sy)
print("Min distance:",d)
