class Person:
	def __init__(self,name,age):
		self.name=name;
		self.age=age;
p1=Person("Suppandi",14)
print("\nName of the person is",p1.name)
print("\nAge of the person is",p1.age)
print("\n***Printing after deleting age attribute for p1***")
del p1.age
print("\nName of the person is",p1.name)
#print("\nAge of the person is",p1.age)
print("\n***Printing after deleting p1***")
del p1
print("\nName of the person is",p1.name)
print("\nAge of the person is",p1.age)
