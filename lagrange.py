from math import prod
def lagrange(x,X,Y):
    fx = 0
    for i in range(len(X)):
        num = prod(x-X[j] for j in range(len(X)) if i != j)
        denom = prod(X[i]-X[j] for j in range(len(X)) if i != j)
        fx += Y[i] * num/denom
    return fx
x = float(input("Enter the value of x: "))
X = list(map(float, input("Enter values of x: ").split()))
Y = list(map(float, input("Enter values of y: ").split()))
print("Interpolation value: ",lagrange(x,X,Y))
