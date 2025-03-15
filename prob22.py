print("Printing current and previous number sum in a range(10)")
for i in range(10):
    j= i-1
    if j <0:
        j=0
    s= i+j
    print("Current Number", i ,"Previous Number",j,"Sum",s)
