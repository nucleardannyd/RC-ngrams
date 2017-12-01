import snap
import random


class Node(object):
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.daysInfected = 0

    def addEdge(self, node):
        self.edges += [node]


class Edge(object):
    def __init__(self, dstNode):
        self.dstNode = dstNode
