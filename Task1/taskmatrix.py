def largest():
    #largest element
    large=mat[0][0]
    for i in range(0,a):
        for j in range(0,i+1):
            if mat[i][j] >= large:
                large=mat[i][j]
                x=i
                y=j
    print("largest number is {},{}= {}".format(x,y,large))

def smallest():
    #finding the smallest element in a matrix
    small=mat[0][0]
    for i in range(0,a):
        for j in range(0,i+1):
            if mat[i][j] <= small:
                small=mat[i][j]
                x=i
                y=j
    print("smallest number is {},{}= {}".format(x,y,small))

def find():
    #finding the element in a matrix
    z=0
    c=int(input("Which number do you want to find"))
    for i in range(0,a):
        for j in range(0,b):
            if mat[i][j]==c:
                x=i
                y=j
                z=1
                print("the element is at ({},{})".format(x,y))
    if z==0:
        print("Number not in array")

def reverse():
    #reversing a matrix
    mat1=[[row[::-1] for row in mat[::-1]]]
    mat3=np.array(mat1)
    print("Your reversed matrix is:\n" ,mat3)   

def rotate():
    #rotating an array around kth position
    k=int(input("Enter the position by which to rotate the matrix"))
    mat2=np.roll(mat, k)
    print(mat2)

name = input("Enter Your Name:").strip().title()
print(f'''Hello!
Welcome to the Program {name}
Here you can perform different functions on an array''')

import numpy as np
a=int(input("Enter the number of rows="))
b=int(input("Enter the number of columns="))
mat=np.zeros(shape=(a,b), dtype = int)
for i in range(0,a):
    for j in range(0,b):
        c=int(input("Enter the number in {},{}=".format(i+1,j+1)))    
        mat[i,j]=c
print(mat)

while True:

    print('''Press the correct option:
    1-To find the largest element in matrix
    2-To find the smallest element in matrix
    3-To find the index of an element in a matrix
    4-To reverse the matrix
    5-To rotate the matrix by k position
    6-End program''')

    ans=int(input("Enter Your option"))

    if ans==1:  
        largest()
    elif ans==2:
        smallest()
    elif ans==3:
        find()
    elif ans==4:
        reverse()
    elif ans==5:
        rotate()
    elif ans==6:
        print("Goodbye")
        break
    else:
        print("Wrong Input")    
