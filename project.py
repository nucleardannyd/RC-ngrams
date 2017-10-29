from struct import Node, Edge, Graph

        
text_file = open("the_mysterious_affair_at_styles.txt", 'r')
text = text_file.read()
text = text.lower()

g = Graph(text, 3, 5)
g.symmetric_window()
g.export("graph.txt")
        


