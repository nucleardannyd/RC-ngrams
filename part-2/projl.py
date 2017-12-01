from graph import *
import sys
import random


if len(sys.argv) < 4:
    print("Script must have 4 arguments.")
    print("python proj.py number_of_infected_acquaintances number_of_days_until_recovery fraction_of_population_required")
    exit(1)

snapGraph = snap.LoadEdgeList(snap.PNGraph, "soc-Epinions1.txt")


n = snapGraph.GetNodes()
b = int(sys.argv[1])
j = int(sys.argv[2])
f = float(sys.argv[3])
t = 1
fraction = 0.0

nodes = []
for NI in snapGraph.Nodes():
    nodes += [Node(NI.GetId())]


for EI in snapGraph.Edges():
    for i in range(len(nodes)):
        if nodes[i].id == EI.GetSrcNId():
            nodes[i].addEdge(nodes[EI.GetDstNId()])


nInfected = 0.0
suceptible = nodes
infected = []
recovered = []

for i in range(b):
    rid = random.randrange(len(suceptible))
    infected += [suceptible[rid]]
    del(suceptible[rid])

t = 1

print fraction
while fraction < f:
    inf = infected
    for i in inf:
        if i.daysInfected == j:
            recovered += [i]
            infected.remove(i)
        else:
            for k in range(b):
                if len(i.edges) > 0:
                    rnode = random.choice(infected[i].edges)
                    if rid in suceptible:
                        infected += rnode
                        suceptible.remove(rnode)
            infected.get(i).daysInfected += 1

    nInfected = float(len(infected.keys()) + len(recovered.keys()))
    fraction = float(nInfected / n)
    print (nInfected)
    print (fraction)
    print (n)
    t += 1

print("It took " + str(t) + " days for " +
      str(f * 100) + "% of people to be infected")
