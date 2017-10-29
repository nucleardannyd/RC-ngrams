import re

class Node:
    def __init__(self, word):
        self.word = word
        self.edges = {}

    def __repr__(self):
        return self.word
        
    def __str__(self):
        s = ""
        if len(self.edges) == 0:
            return self.word + " with 0 edges"
        for e in self.edges.values():
            s += self.word + " -> " + e.getChild().getWord() + "\tWeight = " + str(e.getWeight()) + '\n'
        return s

    # def getInfo(self):
    #     return "Node has " + 
    
    def getWord(self):
        return self.word

    def getEdges(self):
        return self.edges
    
    def getEdge(self, word):
        if word in self.edges.keys():
            return self.edges[word]
    
    def addEdge(self, edge):
        self.edges[edge.getChild().getWord()] = edge

    def getMostCommon(self):
        node = None
        weight = 0
        for i in self.edges.value:
            if i.weight > weight:
                node = [i]
            elif i.weight == weight:
                node += [i]
        return node
        

        
class Edge:
    def __init__(self,child, weight):
        self.child = child
        self.weight = weight
        
    def getChild(self):
        return self.child

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight
    
    def incrementWeight(self):
        self.weight+=1

class Graph:
    def __init__(self, text, n, d):
        self.n = n
        self.d = d
        self.preprocess(text)
        #self.extract_ngrams()
        #self.create_nodes()

    def preprocess(self,text):
        text = re.sub("\,|--+", "", text)
        self.phrases = re.split("[\n.?!;]*", text)
        #        self.phrases = ["<s>"] + self.phrases + ["</s>"]

    def getPhrases(self):
        return self.phrases
        
    def getNgrams(self):
        return self.ngrams

    def getNodes(self):
        return self.nodes

    def getN(self):
        return self.n

    def getD(self):
        return self.d

    def extract_ngrams(self):
        self.ngrams = []
        for p in self.phrases:
            words = p.split("\s")
            s = " "
            for i in range(len(words)-self.n+1):
                self.ngrams += [s.join(words[i:i+self.n])]
                
    def create_nodes(self):
        self.nodes = {}
        for n in self.ngrams:
            if n not in self.nodes.keys():
                self.nodes[n] = Node(n)
        

    def nonsymmetric_window(self):
        for i in range(len(self.ngrams)):
            for j in range(1, self.d+1):
                if (i-j) < 0:
                    break
                elif self.ngrams[i-j] in self.nodes[self.ngrams[i]].getEdges().keys():
                    self.nodes[self.ngrams[i]].getEdge(self.ngrams[i-j]).incrementWeight()
                else:
                    self.nodes[self.ngrams[i]].addEdge(Edge(Node(self.ngrams[i-j]), 1))
        
    def symmetric_window(self):
        for i in range(len(self.ngrams)):
            for j in range(1, (self.d+2)//2):
                if not (i-j) < 0:
                    if self.ngrams[i-j] in self.nodes[self.ngrams[i]].getEdges().keys():
                        self.nodes[self.ngrams[i]].getEdge(self.ngrams[i-j]).incrementWeight()
                    else:
                        self.nodes[self.ngrams[i]].addEdge(Edge(Node(self.ngrams[i-j]), 1))
                if not (i+j) > len(self.ngrams)-1:
                    if self.ngrams[i+j] in self.nodes[self.ngrams[i]].getEdges().keys():
                        self.nodes[self.ngrams[i]].getEdge(self.ngrams[i+j]).incrementWeight()
                    else:
                        self.nodes[self.ngrams[i]].addEdge(Edge(Node(self.ngrams[i+j]), 1))
        
