#Exercise 21: Check if a user-entered string contains any digits using a for loop


str1 = "Pynative123Python"
for i in str1:
    if i.isdigit():
        print("String has numbers")
        break
#    if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#        print("String has numbers")
#        break
else:
    print("String does not have numbers")

