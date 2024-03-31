def picards(eq,x0,y0,n,x):
    x_val = [x0]
    y_val = [y0]
    h = (x-x0)/n
    for i in range(n):
        x_new = x_val[i] + h
        y_new = y0 + integrate(eq(x,y_val[i]),x0,x_new)
        x_val.append(x_new)
        y_val.append(y_new)

    return x_val,y_val
def integrate(eq,l,u):
    h = float((u-l)/6)
    func = lambda x: eq
    res = func(l) + func(u)
    x = l
    for i in range(1,7):
        x += h
        if(i%2!=0):
            
            #print(func(eq,x))
            res += 4*func(x)
        else:
           # print(func(eq,x))
            res += 2*func(x)

    return (h/3 * res)

equation = input("Enter the equation: ")
eq = lambda x,y: eval(equation)
x_val,y_val = picards(eq,1,2,5,1.75)
for i in range(len(x_val)):
    print(f"x:{x_val[i]}\ty:{y_val[i]}")
