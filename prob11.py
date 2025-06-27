#Exercise 11: Get each digit from a number in the reverse order.
a=126
rev=0
while a>0:
    rem=a%10
    rev=(rev*10)+rem
    a=a//10
print(rev)
