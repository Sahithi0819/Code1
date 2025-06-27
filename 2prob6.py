#Exercise 6: Write all content of a file into a new file by skipping line number 5

with open("2prob6.txt","r") as file:
    with open("new_file.txt","w") as file1:
        con=file.readlines()
        for i in con:
            if i!="line5\n":
                file1.write(i)
