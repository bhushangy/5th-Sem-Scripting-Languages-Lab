lis = []
new_lis = []
lis_com = []
n = int(input('enter size: ')) 
print("enter elements:") 
for i in range(0, n): 
    ele = int(input()) 
    lis.append(ele)
      
print(lis) 
	


def remove_dup():
	for i in lis:
		if i in new_lis:
			continue
		else:
			new_lis.append(i)
			

remove_dup()
print(new_lis)
#===========================================================================
#LIST COMPREHENSION
#===========================================================================
#list comprehension...here x is iterator..imp in data science and ML
#Comprehensions in Python provide us with a short and concise way to construct new sequences 
#(such as lists, set, dictionary etc.) using sequences which have been already defined. 
#output_list = [output_exp for var in input_list if (var satisfies this condition)]
#2 types usually used are - [var**2 for var in range(1, 10)] and [var for var in input_list if var % 2 == 0] 

lis_com = [x for x in new_lis if x%2==0]
print(lis_com)
lis_com.reverse()
print(lis_com)
