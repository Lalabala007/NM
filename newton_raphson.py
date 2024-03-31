import sympy as sp 
x = sp.Symbol('x')

def newton_raphson(exp,x0,n):
    f = lambda x: eval(exp)
    exp1 = sp.diff(f(x),x)
    f1 = lambda x: eval(str(exp1))
    for i in range(n):
        new_x = x0 - f(x0)/f1(x0)
        if(x0 == new_x):
            print("Root: " + new_x)
            return
        else:
            x0 = new_x
    else:
        print("Root: ",new_x)

newton_raphson("x*x-2",1,10)
