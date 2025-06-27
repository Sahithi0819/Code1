#Exercise 16: Check Palindrome Number

num=121
pal=0
original=num

while num>0:
    rem=num%10
    pal=(pal*10)+rem
    num=num//10
#print(pal)
if original==pal:
    print("its pal")
else:
    print("not a pal")


#num=input("Enter a number: ")
#lis=list(num)
#if lis == lis[::-1]:
#    print("Number is Palindrome")
#else:
#    print("No")
