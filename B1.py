input('enter elements to list\n')
lis = []
new_lis = []
lis_com = []
for i in range(5):
	inp = int(input())
	lis.append(inp)
	

print(lis)


def remove_dup():
	for i in lis:
		if i in new_lis:
			continue
		else:
			new_lis.append(i)
			




remove_dup()
print(new_lis)
	
#list comprehension...here x is iterator..imp in data science and ML
lis_com = [x for x in new_lis if x%2==0]
print(lis_com)
lis_com.reverse()
print(lis_com)
