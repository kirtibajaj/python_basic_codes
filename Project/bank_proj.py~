import time
d={'name':['A'],'password':['abcd'],'init_bal':[10000],'acc_no':[1001]}
def home():
    __import__('os').system("reset")
    print("\n\n\n")
    print("WELCOME to BANK!!!".center(145,"*"))
    print("\n")
    print("1.LOG-IN".center(145))
    print("\n")
    print("2.SIGN-UP".center(145))
    print("\n")
    print("3.EXIT".center(145))
    print("\n\n\n\n")
    ch=int(input("Enter your choice : ".rjust(60)))
    return ch
def chk_acc(acc):
    if acc in d['acc_no']:
        i=d['acc_no'].index(acc)
        password=input("Enter password : ".rjust(60))
        ch=chk_pass(password,i)
        if ch==1:
            return 2
        elif ch==0:
            return 3
    else:
        return 1
def chk_pass(password,i):
    if password==d['password'][i]:
            return 1
    else:
        return 0
def choices():
    __import__('os').system("reset")
    print("\n\n")
    print("CHOICES".center(145,"*"))
    print("\n")
    print("\n")
    print("1.DEBIT".center(145))
    print("\n")
    print("2.CREDIT".center(145))
    print("\n")
    print("3.CHECK_BALANCE".center(145))
    print("\n")
    print("4.Change password".center(145))
    print("\n")
    print("5.EXIT".center(145))
    print("\n\n\n\n")
    n=int(input("Enter your CHOICE : ".rjust(60)))
    return n
import os
ch=home()
while ch!=3:
    if ch==1:
        print("\n")
        __import__('os').system("reset")
        print("\n\n\n\n\n")
        acc=int(input("Enter account_number : ".rjust(60)))
        print("")
        cho=chk_acc(acc)
        if cho==1:
            __import__('os').system("reset")
            print("\n\n\n\n\n")
            print("Sorry incorrect Account number...Try Again!!!!!".center(145))
            time.sleep(3)
            ch=home()
        elif cho==3:
            print("\n\n\n\n\n")
            __import__('os').system("reset")
            print("\n\n\n\n\n\n")
            print("Your password is incorrect ....check again!!!!!!!".center(145))
            time.sleep(3)
            ch=home()
            break
        else:
            __import__('os').system("reset")
            print("\n\n\n\n\n")
            print("You are log-in successfully!!!".center(145))
            time.sleep(3)
            __import__('os').system("reset")
            n=choices()
            while n!=5:
                i=d['acc_no'].index(acc)
                if n==1:
                    __import__('os').system("reset")
                    print("\n\n\n\n\n")
                    amt=int(input("Enter amount : ".rjust(60)))
                    if amt>d['init_bal'][i]:
                        print("\n\n\n")
                        print("Your account has {} balance....... go wisely!!!".format(d['init_bal'][i]).center(100))
                        time.sleep(3)
                        n=choices()
                    else:
                        print("\n\n")
                        d['init_bal'][i]-=amt
                        print("Your current balance is : {}".format(d['init_bal'][i]).center(100))
                        time.sleep(3)
                        n=choices()
                elif n==2:
                    print()
                    print()
                    __import__('os').system("reset")
                    print("\n\n\n\n\n")
                    amt=float(input("Enter amount : ".rjust(60)))
                    d['init_bal'][i]+=amt
                    print("\n\n")
                    print("Your current balance is:{}".format(d['init_bal'][i]).center(100))
                    time.sleep(3)
                    n=choices()
                elif n==3:
                    __import__('os').system("reset")
                    print("\n\n\n\n\n")
                    print("Your current balance is : {}".format(d['init_bal'][i]).center(145))
                    time.sleep(3)
                    n=choices()
                elif n==4:
                    __import__('os').system("reset")
                    print("\n\n\n\n\n")
                    pswd=input("Enter your new password : ".rjust(60))
                    d['password'][i]=pswd
                    print("\n\n\n")
                    print("Your password is changed".center(100))
                    time.sleep(3)
                    n=choices()
            else:
                ch=home()
    elif ch==2:
        __import__('os').system("reset")
        print("\n\n\n\n\n")
        name = input("Enter name : ".rjust(60))
        print()
        password = input("Enter password : ".rjust(60))
        print()
        bal = int(input("Enter balance to deposit : ".rjust(60)))
        acc = d['acc_no'][-1] + 1
        d['name'].append(name)
        d['password'].append(password)
        d['init_bal'].append(bal)
        d['acc_no'].append(acc)
        __import__('os').system("reset")
        print("\n\n\n\n\n\n\n\n")
        print("Account Created Sucessfully".center(145,"*"))
        print("\n\n")
        print("your Account Number  is : {} ".format(acc).center(145))
        time.sleep(5)
        ch=home()
    elif ch==3:
        pass
    else:
        __import__('os').system("reset")
        print("\n\n\n\n\n")
        print("Invalid input".center(145))
        time.sleep(3)
        ch=home()
else:
    print("\n")
    print("You are out!!!")
    print("Thanks for visiting us..........")
    print("\n")
        
        
