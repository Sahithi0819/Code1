#Exercise 17: Generate Fibonacci series up to 15 terms

num1=0
num2=1
print(num1,num2,end=" ")
for i in range(13):
        r=num1+num2
        num1=num2
        num2=r
        print(r,end=" ")
