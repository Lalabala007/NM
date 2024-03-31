from math import *
def runge_kutta_4(f,x0,y0,h,n):
    x_val = [x0]
    y_val = [y0]
    for i in range(n):
        k1 = h*f(x_val[i],y_val[i])
        k2 = h*f(x_val[i]+(h/2),y_val[i]+(k1/2))
        k3 = h*f(x_val[i]+(h/2),y_val[i]+(k2/2))
        k4 = h*f(x_val[i]+h,y_val[i]+k3)
        x_new = x_val[i] + h
        y_new = y_val[i] + (1/6)*(k1+2*k2+2*k3+k4)

        x_val.append(x_new)
        y_val.append(y_new)
    return x_val,y_val
eq = input("Enter the differential equation in x and y: ")
equation = lambda x,y:eval(eq)
x0 = float(input("Enter the value of x0: "))
y0 = float(input("Enter the value of y0: "))
h = float(input("Enter the step size(h): "))
n = int(input("Enter the no of iterations: "))
x_val,y_val = runge_kutta_4(equation,x0,y0,h,n)
print("Result: ")
for i in range(len(x_val)):
    print(f"Iteration{i+1}: x:{x_val[i]}\ty:{y_val[i]}")
