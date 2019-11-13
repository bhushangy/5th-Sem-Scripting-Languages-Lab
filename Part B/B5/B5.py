fh = open('f.txt')
rd = fh.read()
lis = []

lis = rd.split()
#print(lis)
dic={}
for i in lis:
    dic[i] = dic.get(i,0)+1

#print(dic)

lis2=[]
lis2 = list(dic.items())
#print(lis2)

lis2 = sorted(lis2,key=lambda x:x[1],reverse=True)
print(lis2)

