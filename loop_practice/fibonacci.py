n=int(input("Enter sum of series"))
a,b=0,1
c=1
s=0
print(a,end=' ')
while s+b<=n:
    s+=b
    print(b,end =' ')
    a,b=b,a+b
    c+=1
print("\n no of terms:",c)
 
