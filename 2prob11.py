#Exercise 11: Percentage Display

num=float(input())
den=float(input())
if den<=0:
    print("denominator should not be zero")
else:
    c=((num/den)*100)
    print(f"The percentage:{c:.2f}%")


