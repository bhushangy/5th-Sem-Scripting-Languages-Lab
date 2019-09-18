fhand = open('random.txt')
x = fhand.read()
#print(x)
#print(len(x))
#difference between open and read
lis = []
new_lis = []
dic = {}
lis = x.split()

for i in lis:
    dic[i] = dic.get(i,0) + 1

new_lis = list(dic.items())
	
#print(lis)
for i in new_lis:
	print(i)
	print('\n')

bigc = None
bigw = None
for key,count in new_lis:
    if bigw is None or count>bigc :
        bigc = count
        bigw = key

print(bigw,(bigc))

	
