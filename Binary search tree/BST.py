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

def inorder(rootnode):
    if not rootnode:
        return
    inorder(rootnode.leftchild)
    print(rootnode.data)
    inorder(rootnode.rightchild)

def postorder(rootnode):
    if not rootnode:
        return
    postorder(rootnode.leftchild)
    postorder(rootnode.rightchild)
    print(rootnode.data)

def search(rootnode,nodevalue):
    if rootnode.data==nodevalue:
        print("found")
    elif rootnode.data>nodevalue:
        if rootnode.leftchild.data==nodevalue:
            print("found")
        else:
            search(rootnode.leftchild,nodevalue)
    else:
        if rootnode.rightchild.data==nodevalue:
            print("found")
        else:
            search(rootnode.rightchild,nodevalue)

n1=BSTNode(None)
insertNode(n1,70)
insertNode(n1,25)
insertNode(n1,26)
insertNode(n1,77)
