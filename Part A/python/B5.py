fh = open('f.txt')
rd = fh.read()
lis = []

lis = rd.split()
dic={}
for i in lis:
    dic[i] = dic.get(i,0)+1

    