def OddRange(a,b):
	list=[]
	while(a<=b):
		if(a%2==0):
			a=a+1
			list.append(a)
		else:
			list.append(a)
			a=a+2
	print(list)
print("Enter two numbers")
a=int(input())
b=int(input())
OddRange(a,b)
