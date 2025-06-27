#Exercise 4: Remove first n characters from a string
str1=str(input("enter string:"))
num=int(input("enter number:"))
if num<len(str1):
    result= str1[num:]
    print(result)
else:
    print("not possible")

