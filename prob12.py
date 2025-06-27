#Exercise 12: Calculate income tax

income=45000
ori=income
if ori>10000:
    income=income-10000
if ori<20000 and ori>10000:
    tax=income*0.10
    print("tax:",tax)
elif ori>20000:
    t=income-10000
    st=(t*0.20)+(10000*0.10)
    print("tax:",st)
else:
    print("no tax")

