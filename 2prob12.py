print(" tell us your option in 1, 2, 3")
op1=int(input("enter option:"))
while True:
    if op1 not in [1,2,3]:
        print("invalid option")
    if op1==1:
        print("say hello")
    elif op1==2:
        num=int(input("enter number:"))
        print(num*num)
    elif op1==3:
        print("exit")
    break



