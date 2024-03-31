#Taylor series
from sympy import sympify,symbols,diff,Function,Derivative
from math import factorial
def taylors(df,xn,x,y,h,order=3,vars='x y'):
  X,Y=symbols(vars)
  YX=Function(Y)(X)
  df=sympify(df).subs(Y,YX)
  n=round((xn-x)/h)
  dfs=[df]
  for _ in range(order-1):
    dfs.append(diff(dfs[-1],X))
  print(f'itr|  {X} | {Y}')
  for i in range(1+n+1):
    yns={YX:y}
    for j in range(order):
      yns[Derivative(YX,(X,j+1))]=dfs[j].subs(yns).subs(X,x)
    x+=h
    y=sum(yn*(h**n)/factorial(n) for n,yn in enumerate(yns.values()))
    print(f'{i:02}  | {x:.8f} | {y:.8f}')
  return y
if __name__=='__main__':
  df=input('Enter the differential:')
  x0=float(input('Enter the initial value of the independent variable:'))
  y0=float(input('Enter the initial value of the dependent variable:'))
  x=float(input('Enter the value to extrapolate:'))
  h=float(input('Enter the step size:'))
  od=int(input('Enter the order of the series:'))
  vars=input('Enter the symbols:')
  print(taylors(df,x,x0,y0,h,od,vars=vars if vars else'x y'))
