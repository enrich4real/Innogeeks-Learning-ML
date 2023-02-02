#finding the element in an array
import numpy as np
mat1=0
a=int(input("Enter the number of rows="))
b=int(input("Enter the number of columns="))
z=0
mat=np.zeros(shape=(a,b), dtype = int)
for i in range(0,a):
    for j in range(0,b):
        c=int(input("Enter the number in {},{}=".format(i+1,j+1)))    
        mat[i,j]=c

k= int((input("Rotate the matrix by what poisition:")))
if k>=0:
    mat1=mat
    for i in range(0,k):
        for j in range(0,b):
            f=i+1
            h=j+1   
            mat1[i][j]=mat[i][j]
        print(mat1)