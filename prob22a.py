str1 = "pynative.com is for python lovers"
c = str1.split()
result = ""
for i in c:
    ca = i.capitalize()
    result = result + ca + " "
print(result.strip())
