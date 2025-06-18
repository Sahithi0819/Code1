str1 = "pynative.com is for python lovers"
new_str=""
list_str=[]
for i in str1:
    if i not in " ":
        new_str+=i
    if i == " ":
        list_str.append(new_str)
        new_str=""
list_str.append(new_str)
# print(list_str)
for i in list_str:
    print(i.capitalize(),end=" ")
