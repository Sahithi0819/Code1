a= "Pynative1Python"

for i in a:
    if i.isdigit():
        print("The string contains at least one digit.")
        break
else:
    print("The string does not contain any digits.")
