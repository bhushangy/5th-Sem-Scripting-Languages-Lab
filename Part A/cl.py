class Person:
	gender=''
	def __init__(self,name,age,gender): #self used to as object reference to determine which object is calling the..  
		self.name = name                                                                              #..constructor
		self.age = age
		self.gender = gender

p1 = Person("Suppandi",14,'m')
p2 = Person("Ramu",12,'f')


print("\nName of Person 1 is ",p1.name)
print("\nAge of Person 1 is ",p1.age)
print("\nGender of Person 1 is ",p1.gender)


print("\nName of Person 2 is ",p2.name)
print("\nAge of Person 2 is ",p2.age)
print("\nGender of Person 2 is ",p2.gender)

p2.age = 10

print("\nModified age of Person 2 is ",p2.age)
