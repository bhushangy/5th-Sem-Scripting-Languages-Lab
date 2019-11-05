from datetime import date

def AgeConvert(dob):
    yr = date.today().year
    lis = dob.split('-')
    print(yr-int(lis[2]))


dob =  input('enter dob in dd-mm-yyyy')
AgeConvert(dob)
