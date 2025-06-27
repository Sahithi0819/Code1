#Exercise 2: Print the Sum of a Current Number and a Previous number

a=int(input("enter the number:"))
print("Printing current and previous number sum in a range",a)

for i in range (0,a):
    pv=i-1
    if pv<0:
        pv=0
    sum=i+pv
    print("current number",i,"previous number",pv, "sum:",sum)

