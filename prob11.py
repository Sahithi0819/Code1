# Get each digit from a number in the reverse order.
a=126
b=str(a)
c=b[::-1]
d=len(c)
for i in range(0,d):
    print(c[i], end=" ")
