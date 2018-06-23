p=int(input("Enter a number:"))
c=0
for i in range(2,p):
    if p%i==0:
        c+=1

if c!=0:
    print("Not Prime Number")
else:
    print("Prime Number")
