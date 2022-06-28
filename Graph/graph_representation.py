class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

customDict={
    'a':["b","c"],
    "b":["a",'d','e'],
    "c":['a','e'],
    "d":['b',"e","f"],
    "e":["d","f"],
    "f":["d","e"]
}
g1=Graph(customDict)
g1.addEdge('e',"c")
print(g1.gdict)