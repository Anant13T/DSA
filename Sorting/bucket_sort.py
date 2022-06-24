import math

def bucketSort(customList):
    noBucket=round(math.sqrt(len(customList)))
    maxValue=max(customList)
    arr=[]
    for i in range(noBucket):
        arr.append([])
    for j in customList:
        index_b=math.ceil(j*noBucket/maxValue)
        