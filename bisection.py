def bisection(f,a,b,itr):
    if(f(a)*f(b)>0):
            raise ValueError("Root doesnt lie in this interval")
    
    print(" itr  |  a  |  b  |  xn  |  fxn  ")
    for i in range(1,itr+1): # (0,itr) (1,itr+1)
        fa = f(a)
        fb = f(b)
        x = (a+b)/2
        fx = f(x)
        print(f"  {i}  |  {a}  |  {b}  |  {x}  |  {fx}  ")

        if(fx == 0):
            print("Root has been found")    
            break
        elif fx*fa>0:
            a=x
            fa = fx
        else:
            b=x
            fb = fx

eq = lambda x: eval("x*x - 3")

bisection(eq,1,2,30)
        
            
