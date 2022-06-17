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