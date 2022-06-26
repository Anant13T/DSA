from cv2 import cuda_BufferPool


def partition(customList,low,high):
    i=low-1
    pivort=customList[high]
    for j in range(low,high):
        if customList[j]<=pivort:
            i+=1
            customList[i],customList[j]=customList[j],customList[i]
    customList[i+1],customList[high]=customList[high],customList[i+1]
    return (i+1)

