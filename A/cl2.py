#concept - use of del function to delete attributes of an object and an object itself

class Person:
	gender=''
	def __init__(self,name,age,gender): 
		self.name = name                                                                              
		self.age = age
		self.gender = gender

p1 = Person("Suppandi",14,'m')


print("\nName of Person 1 is ",p1.name)
print("\nAge of Person 1 is ",p1.age)


del p1.age

print("\nName of Person 1 is ",p1.name)
#print("\nAge of Person 1 is ",p1.age)
#======================================================
# ERROR
#Traceback (most recent call last):
#  File "cl2.py", line 18, in <module>
#   print("\nAge of Person 1 is ",p1.age)
#AttributeError: 'Person' object has no attribute 'age'
#======================================================

del p1
print("\nPrinting after deleting object p1\n")
print("\nName of Person 1 is ",p1.name)

#======================================================
# ERROR
#File "cl2.py", line 29, in <module>
#    print("\nName of Person 1 is ",p1.name)
#NameError: name 'p1' is not defined
#======================================================

