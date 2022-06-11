class Treenode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

new1=Treenode('drinks')
lchild=Treenode("cold")
rchild=Treenode("hot")
new1.leftchild=lchild
new1.rightchild=rchild

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

#preorderTraversal(new1)
#inorderTraversal(new1)