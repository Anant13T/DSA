class Heap:
    def __init__(self,size):
        self.customList=(size+1)*[None]
        self.heapSize=0
        self.maxSize=size+1

def peekofHeap(rootnode):
    if not rootnode:
        return
    else:
        return rootnode.customList[1]

def sizeofHeap(rootnode):
    if not rootnode:
        return
    else:
        return rootnode.heapSize

def levelorderTraversal(rootnode):
    if not rootnode:
        return
    else:
        for i in range(1,rootnode.heapSize+1):
            print(rootnode.customList[i])

def heapifyTreeInsert(rootNode,index,heapType):
    parentIndex=int(index/2)
    if index<=1:
        return
    if heapType=='Min':
        if rootNode.customList[index]<rootNode.customList[parentIndex]:
            temp=rootNode.customList[index]
            rootNode.customList[index]=rootNode.customList[parentIndex]
            rootNode.customList[parentIndex]=temp
        heapifyTreeInsert(rootNode,parentIndex,heapType)
    elif heapType=="Max":
        if rootNode.customList[index]>rootNode.customList[parentIndex]:
            temp=rootNode.customList[index]
            rootNode.customList[index]=rootNode.customList[parentIndex]
            rootNode.customList[parentIndex]=temp
        heapifyTreeInsert(rootNode,parentIndex,heapType)

def insertNode(rootNode,nodevalue,heapType):
    if rootNode.heapSize+1==rootNode.maxSize:
        return "the binary heap is full"
    rootNode.customList[rootNode.heapSize+1]=nodevalue
    rootNode.heapSize+=1
    heapifyTreeInsert(rootNode,rootNode.heapSize,heapType)
    return "inserted"

def heapifyTreeExtract(rootNode,index,heapType):
    leftIndex=index*2
    rightIndex=index*2+1
    swapChild=0
    if rootNode.heapSize<leftIndex:
        return
    elif rootNode.heap==leftIndex:
        if heapType=="Min":
            if rootNode.customList[index]>rootNode.customList[leftIndex]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[leftIndex]
                rootNode.customList[leftIndex]=temp
            return 
        else:
            if rootNode.customList[index]>rootNode.customList[leftIndex]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[leftIndex]
                rootNode.customList[leftIndex]=temp
            return  

# h1=Heap(5)
# insertNode(h1,80,"Max")
# insertNode(h1,75,"Max")
# insertNode(h1,95,"Max")
# insertNode(h1,55,"Max")
# insertNode(h1,25,"Max")
# levelorderTraversal(h1)