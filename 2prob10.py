#Exercise 10: Read Line Number 4 from File


with open("2prob6.txt","r") as file2:
    content=file2.readlines()
    for i in content:
        if i=="line4\n":
            print(i)
