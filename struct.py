class Node:
    def __init__(self, word):
        self.word = word
        self.edges = []


    def __str__(self):
        p=""
        for i in self.edges:
            p += self.word + " -> "
            for j in range(i.getLength()-1):
                p += i.getChild(j).getWord() + " -> "
            p += i.getChild(i.getLength()-1).getWord() + '\n'
        return p
        
    def getWord(self):
        return self.word

    def getEdges(self):
        return self.edges
    
    def getEdge(self, edgenum):
        return self.edges[edgenum]
    
    def addEdge(self, edge):
        self.edges += [edge]


        
class Edge:
    def __init__(self,parent,childs):
        self.parent = parent
        self.childs = childs
        self.length = len(childs)
        
    def getParent(self):
        return self.parent

    def getNextChild(self):
        return self.childs[0]

    def getChilds(self):
        return self.childs
    
    def getChild(self, i):
        return self.childs[i]

    def getLength(self):
        return self.length
