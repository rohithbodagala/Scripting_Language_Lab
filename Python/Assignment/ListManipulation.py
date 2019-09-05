list1= ["lion", "tiger", "monkey","Rohith","Sonika"]
print(len(list1))
print(list1[slice(0,4,2)])
list1[1]="banana"
print(list1)
list2 = ["cherry","strawberry"]
list1=list1+list2
print(list1)
list3=list1.copy()
print(list3)
list4=["value1","value2","value3","value4","value5","value6","value7"]
for i in range(0, len(list1)):
	list4[i]=list1[i]
print(list4)
my_list = ['geeks', 'for', 'geeks', 'like', 
		'geeky','nerdy', 'geek', 'love', 
			'questions','words', 'life'] 

# Yield successive n-sized 
# chunks from l. 
def divide_chunks(l, n): 
	
	# looping till length l 
	for i in range(0, len(l), n): 
		yield l[i:i + n] 

# How many elements each 
# list should have 
n = 5

x = list(divide_chunks(my_list, n)) 
print (x) 

