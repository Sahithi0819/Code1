#Exercise 23: Create a simple countdown timer using a while loop.

sec = int(input("Enter the timer value:"))
while sec>0:
    print("Time remaining: ", sec, " seconds")
    sec= sec-1
print("Time's up!")
