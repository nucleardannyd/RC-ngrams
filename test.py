from struct import Node, Edge

o = Node("O")
joao = Node("Joao")
miguel = Node("Miguel")
come = Node("come")
feijao = Node("feijao")
verde = Node("verde")
todos = Node("todos")
os = Node("os")
dias = Node("dias")
sopa = Node("sopa")

o.addEdge(Edge(o, [joao, come, sopa]))
o.addEdge(Edge(o, [miguel, come, feijao, verde, todos, os, dias]))
print(o)
