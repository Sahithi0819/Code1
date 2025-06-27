#Exercise: 19: Print Alternate Prime Numbers till 20

list_1=[]
for i in range(2,20):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        list_1.append(i)
print("All prime numbers from 1 to 20:",list_1)
print("Alternate prime numbers from 1 to 20:",list_1[0::2])
