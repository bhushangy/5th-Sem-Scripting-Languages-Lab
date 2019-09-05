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
		
	def accept(self):
		self.name = input("\n enter name: ")
		self.age = input("\n enter age: ")
		self.marks = input("\n enter marks: ")
		
 


ob1 = Student('',0,[])
ob2 = Student('',0,[])

ob1.accept()
ob1.display()
ob2.accept()
ob2.display()




