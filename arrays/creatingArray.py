from array import *
arr1=array('i',[10,20,30,40,50])
arr2=array('i',[9,8,7,3,1])
print(arr2)

#insertion in the array
arr1.insert(4,6) # this will add 6 in the index position of 4 and shift the other element to the right
print(arr1)

arr1.insert(0,0) # this will add 6 in the index position of 4 and shift the other element to the right
print(arr1)

#traversal of array
def traverseArray(array):
    for i in array:
        print(i)

#traverseArray(arr1)

def accessElement(array,index):
    if index>len(array):
        print("invalid value")
    else:
        print(array[index])

#accessElement(arr1,4)

def findElement(array,num):
    for i in range(len(array)-1):
        if array[i]==num:
            print("value exist at index {}".format(i))
###        else:
###            print("value doesn't exist")

#findElement(arr1,10)

arr1.remove(10) #this will delete the element 10 and move all the element towards left
print(arr1)