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

n1=Trie()
n1.insertString("app")
n1.insertString("appl")