class binaryTree:
    def __init__(self,size):
        self.customlist=size*[None]
        self.lastusedindex=0
        self.maxsize=size
    
    def insertnode(self,value):
        if self.lastusedindex+1==self.maxsize:
            return "full"
        self.customlist[self.lastusedindex+1]=value
        self.lastusedindex+=1

    def search(self,nodevalue):
        for i in range(len(self.customlist)):
            if self.customlist[i]==nodevalue:
                return "found"
        return "not found"

    def levelorderTraversal(self,index):
        for i in range(index,self.lastusedindex+1):
            print(self.customlist[i])

    def deletenode(self,value):
        if self.lastusedindex==0:
            return "empty"
        else:
            for i in range(1,self.lastusedindex):
                if self.customlist[i]==value:
                    self.customlist[i]=self.customlist[self.lastusedindex]
                    self.customlist[self.lastusedindex]=None
                    self.lastusedindex-=1

new1=binaryTree(10)
new1.insertnode(1)
new1.insertnode(2)
new1.insertnode(3)
new1.insertnode(4)
new1.deletenode(2)
new1.levelorderTraversal(1)