def bis(f,xl,xu,n):
    for i in range(n):
        fxl = round(f(xl),4)
        fxu = round(f(xu),4)
        xn = round(((xl*fxu-xu*fxl)/(fxu-fxl)),4)
        fxn = round(f(xn),4)
        print(f"xl:{xl}\txu:{xu}\txn:{xn}\tfxn:{fxn}")
        if(fxn==0):
            print(f"Root is {xn}")
            return 
        elif(fxn*fxl > 0):
            xl = xn
            fxl = fxn
        else:
            xu = xn
            fxu = fxn
    else:
        print(f"Root is {xn}")
f = lambda x:eval("x*x-3")
bis(f,1,2,10)
