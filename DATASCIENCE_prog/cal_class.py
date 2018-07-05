import math
n=int(input("Enter:"))
for i in range(n):
    if pow(2,i)>=n:
        print(i)
        break

print(round(1+3.322*math.log(n,10)))
