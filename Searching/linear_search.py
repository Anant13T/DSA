def linearSearch(array,value):
    for i in range(len(array)):
        if array[i]==value:
            return i
    return -1

print(linearSearch([2,3,4,5,41,43,11,12,34,454,1],1))