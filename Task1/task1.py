import numpy as np
# Searching Element
def search(arr,size,s):
    for i in range(size):
        if(arr[i]==s):
            return i
    return -1

# Find the largest number
def largest(arr,size):
    max=arr[0]
    for i in arr:
        if i>max:
            max=i
    return max

# find smallest number
def smallest(arr,size):
    min=arr[0]
    for i in arr:
        if i<min:
            min=i
    return min

# reverse array
def reverse(arr,size):
    return arr[::-1]

# rotate the array
def rotate(arr,size,k):
    k=k%size
    for i in range(k):
        t=arr[size-1]
        for j in range(size-1,0,-1):
            arr[j]=arr[j-1]
        arr[0]=t
    return arr

#Welcoming to the program

name = input("Enter your name ").strip().title()
print(f"Welcome to the program {name}", end=':)\n')

#initialize and input an array
arr=np.array([],dtype='i')
size=int(input('Enter the size of the array - '))
print('Input '+str(size)+' array elements:')
for i in range(size):
    arr=np.append(arr,int(input()))


#Printing the operation menu

while True:
    print('''1- Find the largest number
2-find the smallest number
3-Find the number in array
4-Reverse the array
5-Rotate the array by k position
6-Close the program''')

    ch=int(input('Input your choice- '))
    if ch==1:
        x=largest(arr,size)
        print('Largest number is: '+str(x))
    

    elif ch==2:
        x=smallest(arr,size)
        print('Smallest number is: ',x)
    
    elif ch==3:
        s=int(input('Number to search in array:'))
        x=search(arr,size,s)
        if x!=-1:
            print('Found at '+str(x+1))
        else:
            print('Not found')
    
    elif ch==4:
        x=reverse(arr,size)
        print('Reversed array: ')
        print(x)
    
    elif ch==5:
        k=int(input('Input the number of rotations: '))
        x=rotate(arr,size,k)
        print('Rotated array: ')
        print(x)    
    elif ch==6:
        break
    
    else:
        print('Invalid choice. TRY AGAIN!!')