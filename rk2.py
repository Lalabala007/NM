from math import *
def runge_kutta_2(f,x0,y0,h,n):
    x_values = [x0]
    y_values = [y0]
    for i in range(0,n):
        k1 = h*f(x_values[i],y_values[i])
        k2 = h*f(x_values[i]+h, y_values[i]+k1)

        y_new = y_values[i] + 0.5*(k1+k2)
        x_new = x_values[i] + h

        x_values.append(x_new)
        y_values.append(y_new)
    return x_values, y_values

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
