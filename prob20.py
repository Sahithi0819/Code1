#Exercise 20: Print Reverse Number Pattern

#for i in range(1,6):
#    for j in range(6-i):
#        print(i,end=" ")
#    print(" ")
c=6
for i in range(1,6):
    c=c-1
    print((str(i)+" ")*c)
