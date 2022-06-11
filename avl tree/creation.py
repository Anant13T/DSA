class AVLtree:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
        self.height=1

def preorderTraversal(rootnode):
    if not rootnode:
        return 
    else:
        print(rootnode.data)
        preorderTraversal(rootnode.leftchild)
        preorderTraversal(rootnode.rightchild)

def inorderTraversal(rootnode):
    if not rootnode:
        return
    else:
        inorderTraversal(rootnode.leftchild)
        print(rootnode.data)
        inorderTraversal(rootnode.rightchild)

def postorderTraversal(rootnode):
    if not rootnode:
        return 
    else:
        postorderTraversal(rootnode.leftchild)
        postorderTraversal(rootnode.rightchild)
        print(rootnode.data)

n1=AVLtree(12)