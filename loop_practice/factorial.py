n=int(input("Enter a number:"))
if n>=0:
    if n>1:
        f=1
        for i in range(1,n+1):
            f=f*i
        print("factorial of {} is:{}".format(n,f))
    else:
        f=1
        print("factorial of {} is:{}".format(n,f))
else:
    print("Negative numbers does not have factorial")

