#Exercise 9: Check File is Empty or Not

import os

size = os.stat("2prob6.txt").st_size
if size == 0:
    print('file is empty')
else:
    print("Not empty")
