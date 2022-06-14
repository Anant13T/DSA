from logging import root
from numpy import insert

class BSTNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

def insertNode(rootNode,nodevalue):
    if rootNode.data==None:
        rootNode.data=nodevalue
    elif nodevalue<=rootNode.data:
        if rootNode.leftchild is None:
            rootNode.leftchild=BSTNode(nodevalue)
        else:
            insertNode(rootNode.leftchild,nodevalue)
    else:
        if rootNode.rightchild is None:
            rootNode.rightchild=BSTNode(nodevalue)
        else:
            insertNode(rootNode.rightchild,nodevalue)
    
def preorder(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preorder(rootnode.leftchild)
    preorder(rootnode.rightchild)

n1=BSTNode(None)
insertNode(n1,70)
insertNode(n1,25)
insertNode(n1,26)
insertNode(n1,77)
preorder(n1)