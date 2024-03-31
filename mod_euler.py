from math import *
def mod_euler(f,x0,y0,n,x):
    x_val = [x0]
    y_val = [y0]
    h = (x-x0)/n
    for i in range(n):
        y_new = y_val[i]+h/2*(f(x_val[i],y_val[i])+f(x_val[i] + h,(y_val[i] + h*f(x_val[i],y_val[i]))))
        x_new = x_val[i] + h
        x_val.append(x_new)
        y_val.append(y_new)
    return y_val[-1]
temp = input("Enter the equation: ")
eq = lambda x,y: eval(temp)
x0 = float(input("Enter the initial value of x: "))
y0 = float(input("Enter the initial value of y: "))
n = int(input("Enter the number of iterations: "))
x = float(input("y(x) for x = "))
print(f"Answer: {mod_euler(eq,x0,y0,n,x)}")
