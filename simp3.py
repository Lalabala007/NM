def func(eq,x):
    eq = eq.replace("x",str(x))
    return float(eval(eq))

def simp3(l,u,n,eq):
    h = float((u-l)/n)
    res = func(eq,l) + func(eq,u)
    x = l
    for i in range(1,n):
        x += h
        if(i%2!=0):
            
            #print(func(eq,x))
            res += 4*func(eq,x)
        else:
           # print(func(eq,x))
            res += 2*func(eq,x)

    return str(h/3 * res)

#eq = input("ENter the equation: ")
eq1 = "1-x-4*x*x*x+2*x*x*x*x*x"
#l =  int(input("Enter the lower limit: "))
l1 = -2
#u =  int(input("Enter the upper limit: "))
u1 = 4
#n = int(input("Enter the number of iterations: "))
n1 = 6
print("Answer: ", simp3(l1,u1,n1,eq1))
