from graph import *
import sys
import random


def infect(node):
	for k in range(b):
		r = random.choice(node.edges)
		if r.id in suceptible.keys():
			infected[r.id] = suceptible[r.id]
			del(suceptible[r.id])	
	
    
if len(sys.argv) < 4:
    print("Script must have 4 arguments.")
    print("python proj.py number_of_infected_acquaintances number_of_days_until_recovery fraction_of_population_required")
    exit(1)

if len(sys.argv) == 5:
	initInfect = int(sys.argv[4])
else:
	initInfect = 0
	
snapGraph = snap.LoadEdgeList(snap.PNGraph, "soc-Epinions1.txt")
rand = snap.TRnd(42)
rand.Randomize()


n = snapGraph.GetNodes()
b = int(sys.argv[1])
j = int(sys.argv[2])
f = float(sys.argv[3])
t = 1
fraction = 0.0

nodes = {}
for NI in snapGraph.Nodes():
    nodes[NI.GetId()] = Node(NI.GetId())

for EI in snapGraph.Edges():
    nodes[EI.GetSrcNId()].addEdge(nodes[EI.GetDstNId()])


nInfected = 0.0
suceptible = nodes
infected = {}
recovered = {}
t = 0

if initInfect != 0:
	for i in range(initInfect):
		rid = snapGraph.GetRndNId()
		if rid in suceptible.keys():
			infected[rid] = suceptible[rid]
			del(suceptible[rid])
	
else:
	rid = snapGraph.GetRndNId()
	rids = infect(suceptible[rid])
	
t = 1

while fraction < f:
	inf = infected.keys()
	print("Nodes infected: " + str(len(inf)))
	for i in inf:
		if infected[i].daysInfected == j:
			recovered[i] = infected[i]
			del(infected[i])
		else:
			if len(infected[i].edges) > 0:
				rids = infect(infected[i])
				infected[i].daysInfected += 1

	nInfected = float(len(infected.keys()) + len(recovered.keys()))
	fraction = float(nInfected / n)
	print (nInfected)
	print (fraction)
	print("Infected: " + str(len(infected)))
	print("recovered: " + str(len(recovered)))
	t += 1

print("It took " + str(t) + " days for " +
      str(f * 100) + "% of people to be infected")
