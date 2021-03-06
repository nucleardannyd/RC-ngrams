import re


class Node:
    def __init__(self, word):
        self.word = word
        self.edges = {}
        self.occurrences = 1

    def __repr__(self):
        return self.word

    def __str__(self):
        if len(self.edges) == 0:
            return self.word
        s = self.word + ":\n"
        for e in self.edges.values():
            s += str(e) + "\n"
        return s

    def getInfo(self):
        a = self.word + "\n" + \
            "Number of Edges:\t" + str(len(self.edges)) + "\n" + \
            "Heaviest Edges:\t"
        for i in self.getMostCommonEdge():
            a += str(i) + "\n"
        a += "Number of occurrences:\t" + str(self.occurrences)
        return a

    def getMostCommonEdge(self):
        # Returns a list of the most common edges of the Node
        node = None
        weight = 0
        for i in self.edges.values():
            if i.weight > weight:
                node = [i]
                weight = i.weight
            elif i.weight == weight:
                node += [i]
        return node


class Edge:
    def __init__(self, parent, child, weight):
        self.parent = parent
        self.child = child
        self.weight = weight

    def __str__(self):
        return self.parent.word + " -> " + self.child.word + "\tWeight: " + str(self.weight)


class Graph:
    def __init__(self, text, n, d):
        self.n = n
        self.d = d
        self.preprocess(text)
        self.extract_ngrams()
        self.create_nodes()

    def preprocess(self, text):

        # Removes special characters
        text = re.sub("[\,():]*", "", text)

        # Substitutes -- for spaces to divide words
        text = re.sub("--+", " ", text)

        # Divides text in phrases
        self.phrases = re.split("[\n.?!;]*", text)

        for p in range(len(self.phrases)):
            self.phrases[p] = re.sub("#", ".", self.phrases[p])

            # Adds <s> and </s> to represent the beginning and end of the phrases
            self.phrases[p] = "<s> " + self.phrases[p] + " </s>"

    def extract_ngrams(self):
        # Extracts ngrams from the list of phrases
        self.ngrams = []
        for p in self.phrases:
            grams = []
            words = re.split("\s+", p)
            s = " "
            for i in range(len(words) - self.n + 1):
                grams += [s.join(words[i:i + self.n])]
            self.ngrams += [grams]

    def create_nodes(self):
        # Creates a Node for each unique word
        self.nodes = {}
        for i in self.ngrams:
            for n in i:
                if n not in self.nodes.keys():
                    self.nodes[n] = Node(n)
                else:
                    self.nodes[n].occurrences += 1

    def nonsymmetric_window(self):
        # Creates the graph using a nonsymmetric window
        for l in self.ngrams:
            for i in range(len(l)):
                for j in range(1, self.d + 1):
                    if (i - j) < 0:
                        break
                    elif l[i - j] in self.nodes[l[i]].edges.keys():
                        self.nodes[l[i]].edges[l[i - j]].weight += 1
                    else:
                        self.nodes[l[i]
                                   ].edges[l[i - j]] = Edge(self.nodes[l[i]], Node(l[i - j]), 1)

    def symmetric_window(self):
        # Creates a graph using a symmetric window
        for l in self.ngrams:
            for i in range(len(l)):
                for j in range(1, (self.d + 2) // 2):
                    if not (i - j) < 0:
                        if l[i - j] in self.nodes[l[i]].edges.keys():
                            self.nodes[l[i]].edges[l[i - j]].weight += 1
                        else:
                            self.nodes[l[i]
                                       ].edges[l[i - j]] = Edge(self.nodes[l[i]], Node(l[i - j]), 1)
                    if not (i + j) > len(l) - 1:
                        if l[i + j] in self.nodes[l[i]].edges.keys():
                            self.nodes[l[i]].edges[l[i + j]].weight += 1
                        else:
                            self.nodes[l[i]].edges[l[i + j]] = Edge(
                                self.nodes[l[i]], Node(l[i + j]), 1)

    def export(self, filename):
        # Exports graph to file
        file = open(filename, 'w')

        # Number of nodes
        file.write(str(len(self.nodes)) + "\n")

        e = 0
        edges = []
        for n in self.nodes.values():
            e += len(n.edges)

        # Number of edges
        file.write(str(e) + "\n")
        # Rank of n-gram
        file.write(str(self.n) + "\n")
        # Window size (Number of Words)
        file.write(str(self.d) + "\n")

        for n in self.nodes.values():
            # Node name and number of occurrences
            file.write(str(n.word) + " " + str(n.occurrences) + "\n")
            edges += n.edges.values()

        for e in edges:
            # Origin node, destination node and weight of the edge
            file.write(str(e.parent.word) + " " +
                       str(e.child.word) + " " + str(e.weight) + "\n")
        file.close()
