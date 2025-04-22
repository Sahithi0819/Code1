num1=1
num2=int(input("Enter base:"))
exp=int(input("Enter Exponant:"))
for i in range(exp):
        r=num1*num2
        num1=r
print(num2,"raises to the power of", exp,":",r)
