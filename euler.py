def euler(f,x0,y0,n,x):
    x_val = [x0]
    y_val = [y0]
    h = (x-x0)/n
    for i in range(n):
        y_new = y_val[i] + h*f(x_val[i],y_val[i])
        x_new = x_val[i] + h
        x_val.append(x_new)
        y_val.append(y_new)
    return x_val,y_val
temp = input("Enter the equation: ")
eq = lambda x,y: eval(temp)
x0 = float(input("Enter the initial value of x: "))
y0 = float(input("Enter the initial value of y: "))
n = int(input("Enter the number of iterations: "))
x = float(input("y(x) for x = "))
x_val,y_val = euler(eq,x0,y0,n,x)

for i in range(len(x_val)):
    print(f"x: {x_val[i]},\ty:{y_val[i]}")
