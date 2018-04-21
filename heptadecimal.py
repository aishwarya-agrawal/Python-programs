def ChangeHept(n):
    if (n <=0):
        return
    elif (n==1):
        print(1,end="")
    else:
        ChangeHept(int( n / 17) )
        x =(n%17)
        if (x < 10):
            print(int(x),end=""), 
        if (x == 10):
            print("a",end=""),
        if (x == 11):
            print("b",end=""),
        if (x == 12):
            print("c",end=""),
        if (x == 13):
            print("d",end=""),
        if (x == 14):
            print("e",end=""),
        if (x == 15):
            print ("f",end=""),
        if (x == 16):
            print("g",end="")
        
ChangeHept(199)

