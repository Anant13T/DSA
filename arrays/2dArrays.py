import numpy as np
from pandas import array
arr1=np.array([[1,2,3],[11,22,33],[9,8,7]])
#print(arr1)
#insertion in the array
new=np.insert(arr1,0,[5,6,7],axis=1)
#append array
new=np.append(arr1,[[10,20,30]],axis=0)
#access an element in an array
def accessElement(array,n1,n2):
    if n1>=len(array) and n2>=len(array[0]):
        print("Invalid input")
    else:
        print(array[n1][n2])
#traversal of array
def travesal(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i][j])
#searching for an element 
def search(array,num):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j]==num:
                print("element present at index[{}][{}]".format(i,j))
#deletion
new1=np.delete(arr1,0,axis=0)# here 0 signifies the row/coloum i want to delete