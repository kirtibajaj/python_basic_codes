p=int(input("Enter a number:"))
for i in range(2,p):
    if p%i==0:
         print("Not Prime Number")
         break
else:
    print("Prime number")
# to print series of prime number in a range
x=int(input("Enter start of series:"))
y=int(input("ENter end of series:"))
for i in range(x,y+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")
