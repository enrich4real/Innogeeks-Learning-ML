#largest element in a array
import numpy as np
a=int(input("Enter the number of rows="))
b=int(input("Enter the number of columns="))
mat=np.zeros(shape=(a,b), dtype = int)
for i in range(0,a):
    for j in range(0,b):
        c=int(input("Enter the number in {},{}=".format(i+1,j+1)))    
        mat[i,j]=c
print(mat)
large=mat[0]
for i in range(0,a):
    for j in range(0,i+1):
        if mat[i][j] >= large:
            large=mat[i][j]
            x=i
            y=j
print("largest number is {},{}= {}".format(x+1,y+1,large))
