str_x = "Emma is good developer. Emma is a writer"
lis1 = []
word = " "
for i in str_x:
    if i != " ":
        word = word+i
    if i == " ":
        lis1.append(word)
        word = " "
lis1.append(word)
# print(lis1)

unique_value=[]
for i in lis1:
    if i not in unique_value:
        unique_value.append(i)
print(unique_value)

counts=[]
for i in unique_value:
    count=0
    for j in lis1:
        if i == j:
            count=count+1
    counts.append(count)
    # print(i,count)
print(counts)
