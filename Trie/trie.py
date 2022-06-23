from jsonschema import RefResolutionError


class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfString=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insertString(self,word):
        current=self.root
        for i in word:
            ch=i
            node=current.children.get(ch)
            if node==None:
                node=TrieNode()
                current.children.update({ch:node})
            current=node
        current.endOfString=True

    def searchString(self,word):
        currentNode=self.root
        for i in word:
            node=currentNode.children.get(i)
            if node==None:
                return False
            currentNode=node
        if currentNode.endOfString==True:
            return True
        else:
            return False

def deleteString(root,word,index):
    ch=word[index]
    currentNode=root.children.get(ch)
    canThis=False
    if len(currentNode.children)>1:
        deleteString(currentNode,word,index+1)
        return False
    if index == len(word)-1:
        if len(currentNode.children)>=1:
            currentNode.endOfString=False
            return False
        else:
            root.children.pop(ch)
            return True
    if currentNode.endOfString==True:
        deleteString(currentNode,word,index+1)
        return False
    canThis=deleteString(currentNode,word,index+1)
    if canThis==True:
        root.children.pop(ch)
        return True
    else:
        return False

n1=Trie()
n1.insertString("app")
n1.insertString("appl")