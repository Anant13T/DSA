def bubble_sort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j]>customList[j+1]:
                customList[j],customList[j+1]=customList[j+1],customList[j]
    print(customList)

l1=[2,4,6,5,4,8,1,0]
bubble_sort(l1)