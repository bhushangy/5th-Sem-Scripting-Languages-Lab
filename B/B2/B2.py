foo = True
tup_lis = []

def C2F():
    C = int(input('Input the Celcius value ').strip())
    F = C * 1.8 + 32
    print(C, "C in Farenheit is ", F)
    tup_lis.append(("C--> ",C," F--> ", F))


def F2C():
    F = int(input('Input the Farenheit value ').strip())
    C = (F - 32) * 0.5556
    print(F, "F in Celcius is ", C)
    tup_lis.append(("F--> ", F, " C--> ", C,))




while foo:
    user_input=int(input("""
        Enter 1 to convert Celcius to Farenheit
        Enter 2 to convert Farenheit to Celcius 
        Enter 3 to sort by from value
        Enter 4 to sort by to value
        Enter 5 to Exit
        """).strip())

    if user_input==1:
        C2F();

    elif user_input==2:
        F2C();
    
    elif user_input==3:
        print(sorted(tup_lis,key = lambda x:x[1]))

    elif user_input==4:
        print(sorted(tup_lis,key = lambda x:x[3]))

    elif user_input==5:
        foo = False
        
