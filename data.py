n=int(input("Enter no of observation : "))
l=[]
for i in range(n):
    d=[]
    d.append(int(input("Enter Age : ")))
    d.append(int(input("Enter Frquency of that age : ")))
    l.append(d)
print("AGE     :     Frequency    :   Fx".center(145))
for i in range(n):
    l[i].append(l[i][0]*l[i][1])
    print(("{}".format(l[i][0])).rjust(60),end="")
    print(("{}".format(l[i][1])).rjust(15),end="")
    print(("{}".format(l[i][2])).rjust(15))
s=0
f=0
for i in range(len(l)):
    s+=l[i][2]
    f+=l[i][1]
print(s/f)






