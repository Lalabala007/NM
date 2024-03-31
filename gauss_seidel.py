def gauss_seidel(mat, n, initial_vector=None):
    eq_x = f"({mat[0][1]*-1}*y + {mat[0][2]*-1}*z + {mat[0][3]})/{mat[0][0]}"
    eq_y = f"({mat[1][0]*-1}*x + {mat[1][2]*-1}*z + {mat[1][3]})/{mat[1][1]}"
    eq_z = f"({mat[2][0]*-1}*x + {mat[2][1]*-1}*y + {mat[2][3]})/{mat[2][2]}"
    f_x = lambda y,z: eval(eq_x)
    f_y = lambda x,z: eval(eq_y)
    f_z = lambda x,y: eval(eq_z)
    if(initial_vector == None):
        x = 0
        y = 0
        z = 0
    else:
        x = initial_vector[0]
        y = initial_vector[1]
        z = initial_vector[2]
    print(f"x:{x}\ty:{y}\tz:{z}")
    for i in range(n):
        prev_x = x
        prev_y = y
        prev_z = z
        x = f_x(y,z) 
        y = f_y(x,z)
        z = f_z(x,y)
        print(f"x:{x}\ty:{y}\tz:{z}")
        if(x == prev_x and y == prev_y and z == prev_z):
            print("Solution Found")
            break

mat = [[20,1,-2,17],[3,20,-1,-18],[2,-3,20,25]]
gauss_seidel(mat,10)
