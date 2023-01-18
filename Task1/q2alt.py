#finding the element in an array
import numpy as np
a=int(input("Enter the number of rows="))
b=int(input("Enter the number of columns="))
z=0
mat=np.zeros(shape=(a,b), dtype = int)
for i in range(0,a):
    for j in range(0,b):
        c=int(input("Enter the number in {},{}=".format(i+1,j+1)))    
        mat[i,j]=c
print(mat)
c=int(input("Which number do you want to find"))
for i in range(0,a):
    for j in range(0,b):
        if mat[i][j]==c:
            x=i+1
            y=j+1
            z=1
            print("the element is at ({},{})".format(x,y))
if z==0:
    print("Number not in array")
