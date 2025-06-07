str_x = "Emma is good sunny developer. sunny Emma is sunny a writer"
word=""
word_list=[]
for i in str_x:
    if i not in (" ","."):
        word+=i
    if i == " ":
        word_list.append(word.lower())
        word=""
if word:
    word_list.append(word.lower())
print(word_list)

count={}
for i in word_list:
    if i in count:
        count[i]+=1
    if i not in count:
        count[i]=1
print(count)

max_list=[]
for i in count:
    max_list.append(count[i])
max_list=sorted(max_list,reverse=True)
print(max_list)
for i in max_list:
   for j,val in count.items():
       if i == val:
           print(j,i)
           max_list.remove(i)

