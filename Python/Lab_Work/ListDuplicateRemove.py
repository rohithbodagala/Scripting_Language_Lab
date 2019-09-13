list1=['cherry','apple','mango','cherry','banana','apple','banana']
print(list1)
list2=[]
for x in list1:
        if x not in list2:
                list2.append(x)
print(list2)
