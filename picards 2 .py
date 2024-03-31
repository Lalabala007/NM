import sympy as sp

exp = "2*x*y"
x = sp.symbols('x')

def picards(x0,y0,xn,n):
    f = lambda x,y: eval(exp)
    yn = y0
    for i in range(n):
        yn = y0 + sp.integrate(f(x,yn),(x,x0,x))
        print(yn)                                                                      
    yn = str(yn)    
    print(eval(yn.replace('x',str(xn))))
picards(1,2,1.75,5)

    