def func(eq,x):
    eq = eq.replace("x",str(x))
    return float(eval(eq))

def trap(l,u,n,eq):
    h = float((u-l)/n)
    res = func(eq,l) + func(eq,u)
    x = l
    for i in range(n-1):
        x += h
        res += 2*func(eq,x)

    return h/2 * res

eq = input("ENter the equation: ")
l =  int(input("Enter the lower limit: "))
u =  int(input("Enter the upper limit: "))
n = int(input("Enter the number of iterations: "))
print("Answer: ", trap(l,u,n,eq))

