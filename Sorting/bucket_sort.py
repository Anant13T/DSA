import math

def insertionSort(customList):
    for i in range(1,len(customList)):
        key=customList[i]
        j=i-1
        while j>=0 and key<customList[j]:
            customList[j+1]=customList[j]
            j-=1
        customList[j+1]=key
    return customList

def bucketSort(customList):
    noBucket=round(math.sqrt(len(customList)))
    maxValue=max(customList)
    arr=[]
    for i in range(noBucket):
        arr.append([])
    for j in customList:
        index_b=math.ceil(j*noBucket/maxValue)
        arr[index_b-1].append(j)
    for i in range(noBucket):
        arr[i]=insertionSort(arr[i])
    k=0
    for i in range(noBucket):
        for j in range(len(arr[i])):
            customList[k]=arr[i][j]
            k+=1
    print(customList)

a1=[54,34,23,1,34,32,90]
bucketSort(a1)