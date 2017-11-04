from struct import Node, Edge, Graph

text_file = open("the_mysterious_affair_at_styles.txt", 'r')
text = text_file.read()
text = text.lower()


g = Graph(text, 3, 4)  # Graph(text, n, D)
# g.symmetric_window()
g.nonsymmetric_window()
g.export("graph.txt")
text_file.close()
