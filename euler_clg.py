from math import *
def runge_kutta_2(f,x0,y0,h,n):
    x_val= [x0]
    y_val = [y0]
    for i in range(0,n):
        y_new = y_val[i] + h*f(x_val[i],y_val[i])
        x_new = x_val[i] + h

        x_val.append(x_new)
        y_val.append(y_new)
    return x_val, y_val

#Get user inputs
equation_input = input("Enter the differential equation in terms of x and y: ")
equation = lambda x,y: eval(equation_input)
x0 = float(input("Enter initial value of x: "))
y0 = float(input("Enter initial value of y: "))
h = float(input("Enter the step size h: "))
n = int(input("Enter the no of iterations: "))
x_val,y_val = runge_kutta_2(equation,x0,y0,h,n)
print("Results: ")
for i in range(len(x_val)):
    print(f"Iterations{i}: x:{x_val[i]}\ty:{y_val[i]}")
