from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes=set()
        self.edges=defaultdict(list)
        self.distances={}

    def addNode(self,value):
        self.nodes.add(value)
    
    def addEdge(self,fromNode,toNode,distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode,toNode)]=distance

def dijkstra(graph,initial):
    visited={initial:0}
    path=defaultdict(list)
    nodes=set(graph.nodes)
    while nodes:
        minNode=None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode=node
                elif visited[node]<visited[minNode]:
                    minNode=node
        if minNode is None:
            break
        nodes.remove(minNode)
        currentWeight=visited[minNode]
        for edge in graph.edges[minNode]:
            weight=currentWeight+graph.distances[(minNode,edge)]
            if edge not in visited or weight<visited[edge]:
                visited[edge]=weight
                path[edge].append(minNode)
    return visited,path

g1=Graph()
g1.addNode("a")
g1.addNode("b")
g1.addNode("c")
g1.addNode("d")
g1.addNode("e")
g1.addNode("f")
g1.addNode("g")
g1.addEdge("a","b",2)
g1.addEdge("a","c",5)
g1.addEdge("b","c",6)
g1.addEdge("b","d",1)
g1.addEdge("b","e",3)
g1.addEdge("c","f",8)
g1.addEdge("d","e",4)
g1.addEdge("e","g",9)
g1.addEdge("f","g",7)
print(dijkstra(g1,"a"))