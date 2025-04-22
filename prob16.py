num=input("Enter a number: ")
lis=list(num)
if lis == lis[::-1]:
    print("Number is Palindrome")
else:
    print("No")
