class Student:
	name=''
	age = 0
	marks = []
	
	def __init__(self,name,age,marks):
		self.name = name                                                                              
		self.age = age
		self.marks = marks



	def display(self):
		print("\n name is ",self.name)
		print("\n name is ",self.age)
		print("\n name is ",self.marks)
		
 

m = []
name = input("\nenter name: ")
age = input("\nenter age: ")
m = input("\nenter marks: ")

ob1 = Student(name,age,m)
#ob2 = Student('',0,[])



