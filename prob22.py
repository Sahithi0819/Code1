#Exercise 22: Capitalize the first letter of each word in a string

str1 = "pynative.com is for python lovers"
wrd=""
lis=[]
for i in str1:
    if i not in " ":
        wrd+=i
    if i ==" ":
        lis.append(wrd)
        wrd=""
lis.append(wrd)

for i in lis:
    print(i.capitalize(),end=" ")


