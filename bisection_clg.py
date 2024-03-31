from sympy import sympify

def bisection(f, a, b, iterations):
    f = sympify(f)
    var, = f.free_symbols
    fa = f.subs(var, a)
    fb = f.subs(var, b)
    
    if fa*fb>=0:
        raise ValueError(f'The root does not lie in the open interval ({a}, {b})')
    
    print(f'itr|     a      |     b      |     {var}')
    for i in range(1, iterations+1):
        x = (a+b)/2
        fx = f.subs(var, x)
        
        print(f'{i:02} | {a:.8f} | {b:.8f} | {x:.8f}')
        
        if fx==0:
            print('Root found: further iterations not possible')
            break
        elif fx*fa<0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx
    
    return x


if __name__=='__main__':
    f = input('Enter the function: ')
    a = float(input('Enter the lower limit: '))
    b = float(input('Enter the upper limit: '))
    itr = int(input('Enter the number of iterations: '))
    print(bisection(f, a, b, itr)) #-2*x**6-1.6*x**4+12*x+1
