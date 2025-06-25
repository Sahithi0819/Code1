with open("sample.txt","r") as file:
    with open("new_file.txt", "w") as file1:
        file_content=file.readlines()
                print(file_content[4])
        


