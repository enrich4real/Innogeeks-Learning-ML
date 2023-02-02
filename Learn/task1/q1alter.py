#finding the largest element in an array
import numpy as np
b=int(input("Enter the number of columns="))
a=int(input("Enter the number of rows="))
mat=np.zeros(shape=(a,b), dtype = int)
for i in range(0,a):
    for j in range(0,b):
        c=int(input("Enter the number in {},{}=".format(i+1,j+1)))    
        mat[i,j]=c
print(mat)
large=np.max(mat)
ind=np.argwhere(mat==large)
print("largest number in array is {} = {}".format(ind,large))

        