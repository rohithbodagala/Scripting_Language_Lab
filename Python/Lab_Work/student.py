students={
	'1MS17IS026':'Anmol',
	'1MS17IS037':'Rohith',
	'1MS17IS050':'Ishank','1MS17IS500':'Sonika'
}
list=["value1","value2","value3","value4"]
list2=[]
j=0
for i in students:
	print("Key is",i,"Value is",students[i])
	list[j]=students[i]
	#list2[j]=i
	j=j+1

print(list)
#print(list2)
print(students.keys())
print(students.values())
print(students.items())
