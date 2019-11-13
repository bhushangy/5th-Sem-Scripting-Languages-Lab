def ls(st):

    for i in range(0,len(st)):
        if st[i].isalpha():
            if st[i].isalpha() and i==0:
                print('False')
                return
            elif st[len(st)-1].isalpha():
                 print('False')
                 return
            elif st[i-1] == '+' and st[i+1] == '+':
                continue
            else:
                 print('False')
                 return
        continue
    print('True')
    

ls('+f+2+e+')