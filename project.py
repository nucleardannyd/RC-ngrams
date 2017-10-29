import re
from struct import Node, Edge, Graph

        
text_file = open("the_mysterious_affair_at_styles.txt", 'r')
text = text_file.read()
text = text.lower()

g = Graph(text, 1, 2)
g.symmetric_window()
print(g.getNodes()["acquitted?"])
print(len(g.getNodes()["acquitted?"].getEdges()))
        


