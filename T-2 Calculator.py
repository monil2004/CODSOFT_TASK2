print(" Enter Two Numbers Below:")
a=int(input("Enter first Number:"))
b=int(input("Enter Second Number:"))
ch=0
while ch<5:
    print("calculator Menu")
    print("1,ADD")
    print("2,SUBTRACT")
    print("3,MULTIPLY")
    print("4,DIVIDE")
    print("5,EXIT")
    ch=int(input("Enter Your Choice;"))
    if ch==1:
        c=a+b
        print("sum:",c)
    elif ch==2:
        c=a-b
        print("SUBTRACT:",c)
    elif Ch==3:
        c=a*b
        print("MULTIPLY:",c)
    elif ch==4:
        c=a/b
        print("DIVIDE:",c)
    elif ch==5:
        break
    else:
        print("wrong choice")
    


