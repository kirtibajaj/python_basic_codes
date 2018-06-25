from random import randint
from random import choice
l=[[1,2,3],[4,5,6],[7,8,9]]
board=[1,2,3,4,5,6,7,8,9]
def print_board():
    print()
    print()
    for i in range(0,3):
        for j in range(0,3):
            print(l[i][j],end=" ")
        print()
    print()
def chk_empty_assign(x,ele):
    chk=0
    for i in range(0,3):
        for j in range(0,3):
            if x==l[i][j]:
                l[i][j]=ele
                chk=1
                board.remove(x)
                return
    if chk==0:
        print("OOPS!!!! this is already filled")
        return
def check_board(step):
    if board==[]:
        print("Its a tie!!!!!!!!!!!")
        return 0
    for i in range(0,3):
        if l[i].count(step)==3:
            print("Player:{} win".format(step))
            return 0
    for i in range(0,3):
        c=0
        for j in range(0,3):
            if l[j][i]==step:
                c+=1
                if c==3:
                    print("Player:{} win".format(step))
                    return 0
    c=0
    for i in range(0,3):
        if l[i][i]==step:
            c+=1
            if c==3:
                print("Player:{} win".format(step))
                return 0
    if l[0][2]==l[1][1]==l[2][0]==step:
        print("Player:{} win".format(step))
        return 0      
    return 1
print("WELCOME to TIC TAC TOE".center(100,"*"))
print_board()
print("Lets assign you as player 1 and you have assigned x")
chance=randint(1,2)
print("As per random toss player:{} win".format(chance))
while board!=[]:
    if chance==1:
        x=int(input("Enter any number its your turn:"))
        chk_empty_assign(x,'x')
        chk=check_board('x')
    else:
        o=choice(board)
        chk_empty_assign(o,'o')
        chk=check_board('o')
    print_board()
    if chance==1:
        chance=2
    else:
        chance=1
    if chk==0:
        break
    else:
        continue
print("Thank you")
