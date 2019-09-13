

lis = []


def ctof(c):
	res = (c*9/5) + 32
	print(res)
	tup = ("celcius:",c,"farenheit:",res)
	lis.append(tup)
	


def ftoc(f):
	res = (f-32)*5/9
	print(res)
	tup = ("farenheit:",f,"celcius:",res)
	lis.append(tup)
	
	


print(" 1) c to f\n 2) f to c \n 3)0 to exit\n")



while 1:
	inp = int(input("enter choice\n"))
	if inp==1:
		print("enter temp in celcius\n")
		cel = int(input())
		ctof(cel)
		
	elif inp==2:
		print("enter temp in fahrenheit\n")
		fah = int(input())
		ftoc(fah)
	
	elif inp==0:
		print(lis)
		break
		
		

		
	


	



