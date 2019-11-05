students = { '1ms17is001':'aaa','1ms17is002':'bbb','1ms17is003':'ccc',
    '1ms17is004':'ddd','1ms17is005':'eee'}

list = ["value1","value2","value3","value4","value5"]
list2 = []
j=0

for i in students:
    print('key is ',i,'value is ',students[i])
    list[j] = students[i]
    list2.append(i)  #no order while traversing the dictionary... You cant assign value to a list "position" if it doesnt exist yet
    j = j + 1




print(list)
print(list2)
    
