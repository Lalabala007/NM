from math import factorial
def forward_interpolation(x,X,Y):
    h = X[1] - X[0]
    n = (x-X[0])/h
    table = [[i for i in Y]]
    for i in range(len(Y) - 1):
        table.append([])
        p1 = 0
        p2 = 1
        while p2 < len(table[i]):
            table[i+1].append(table[i][p2] - table[i][p1])
            p1 += 1
            p2 += 1
    fa = 0
    for i in range(len(Y)):
        res = n
        if i == 0:
            fa += table[i][0]
        else:
            temp = n
            for j in range(i-1):
                temp -= 1
                res *= temp
            fa +=res* table[i][0] / factorial(i)
    print(fa)

x = 1955
X = [1951,1961,1971,1981]
Y = [35,42,58,84]
forward_interpolation(x,X,Y)    