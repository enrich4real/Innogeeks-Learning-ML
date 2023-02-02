#finding the smallest element in a matrix
import numpy as np
a=int(input("Enter the number of rows="))
b=int(input("Enter the number of columns="))
mat=np.zeros(shape=(a,b), dtype = int)
for i in range(0,a):
    for j in range(0,b):
        c=int(input("Enter the number in {},{}=".format(i+1,j+1)))    
        mat[i,j]=c
print(mat)
small=np.min(mat)
ind=np.argwhere(mat==small)
print("smallest number in array is {} = {}".format(ind,small))