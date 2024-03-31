def secant(f,xl,xu,n):
    for i in range(n):
        fxl= round(f(xl),4)
        fxu = round(f(xu),4)
        xn = round((xl*fxu - xu*fxl)/(fxu-fxl),4)
        print(f"xl:{xl}\txu:{xu}\txn:{xn}")
        if(xu==xn):
            print(f"Root:{xn}")
            return xn
        else:
            xl = xu
            xu = xn
    else:
        print(f"Root: {xn}")
exp = input("Expression: ")
f = lambda x: eval(exp)
xl = float(input("Lower Limit: "))
xu = float(input("Upper limit: "))
n = int(input("No of iteration: " ))
secant(f,xl,xu,n)
