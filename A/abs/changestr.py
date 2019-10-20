# here whenever u modify a string... the changes do not appear in the original string...
# thus u gotta append chages to a new string char by char newstr+=' ' 




def ChangeString(s):
    lis1=[]
    for i in s:
        if i.isalpha():
            lis1.append(ord(i))
        else:
            lis1.append(i)
    ns=''  
    for i in lis1:
        try:
            i+=1
            ns+=chr(i)
        except:
            ns+=i
            
    lis2=[]
    for i in ns:
        if i=='{': 
            lis2.append('a')
        elif i=='[':
            lis2.append('A')
        else:
            lis2.append(i)
    nns = ''
    for i in lis2:
        nns+=i
    
    print(nns)




ChangeString('hello*3')