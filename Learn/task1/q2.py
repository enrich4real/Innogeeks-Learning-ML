#finding the element in an array
import numpy as np
a=int(input("Enter the number of rows="))
b=int(input("Enter the number of columns="))
mat=np.zeros(shape=(a,b), dtype = int)
for i in range(0,a):
    for j in range(0,b):
        c=int(input("Enter the number in {},{}=".format(i+1,j+1)))    
        mat[i,j]=c
print(mat)
print("which element do you want to find")
c=int(input("Enter row"))
d=int(input("Enter column"))
if c>a and d>b:
    print("not found")
else:
    print(mat[c-1][d-1])
c=np.argwhere()