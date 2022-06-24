def selection(customList):
    for i in range(len(customList)):
        minIndex=i
        for j in range(i+1,len(customList)):
            if customList[minIndex]>customList[j]:
                minIndex=j
        customList[i],customList[minIndex]=customList[minIndex],customList[i]
    print(customList)

a1=[2,1,3,1,5,6,7,4,5,8]
selection(a1)