class Student:
	def __init__(self,name,age,l):
		self.name=name;
		self.age=age;
		self.l=l;
	def display(self):
		print("Name: ",self.name,";Age: ",self.age,";Marks: ",self.l)
		
s1=Student("Rohith",19,[89,92,94])
s2=Student("Anmol",20,[73,85,91])
s1.display()
s2.display()
	
