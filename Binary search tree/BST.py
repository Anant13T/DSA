from numpy import insert

class BSTNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

    def insertNode(self,rootNode,nodevalue):
        if rootNode.data==None:
            rootNode.data=nodevalue
        elif nodevalue<=rootNode.data:
            if rootNode.leftchild==None:
                rootNode.leftchild=BSTNode(nodevalue)
            else:
                insert(rootNode.leftchild.nodevalue)
        else:
            if rootNode.rightchild==None:
                rootNode.rightchild=BSTNode(nodevalue)
            else:
                insert(rootNode.rightchild.nodevalue)
    


n1=BSTNode(None)
n1.insertNode(n1,70)
n1.insertNode(n1,25)