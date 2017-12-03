from graph import *
import sys
import random

def infect(node):
	repeated = 0
	for k in range(b):
		if len(node.edges) != 0:
			r = random.choice(node.edges)
			if r.id in suceptible.keys():
				infected[r.id] = suceptible[r.id]
				del(suceptible[r.id])	
			elif r.id in infected.keys():
				repeated += 1
	return repeated
    
if len(sys.argv) < 5:
    print("Script must have 5 arguments.")
    print("python proj.py number_of_infected_acquaintances number_of_days_until_recovery number_of_initial_infected_nodes function_to_use")
    exit(1)

	
snapGraph = snap.LoadEdgeList(snap.PNGraph, "soc-Epinions1.txt")

n = snapGraph.GetNodes()
b = int(sys.argv[1])
j = int(sys.argv[2])
initInfect = int(sys.argv[3])
function = sys.argv[4]
t = 1
rand = snap.TRnd(42)
rand.Randomize()
#fraction = 0.0

if initInfect > n:
	initInfect = n
nodes = {}
for NI in snapGraph.Nodes():
    nodes[NI.GetId()] = Node(NI.GetId())

for EI in snapGraph.Edges():
    nodes[EI.GetSrcNId()].addEdge(nodes[EI.GetDstNId()])



suceptible = nodes
infected = {}
recovered = {}
t = 0
repeated = 0
if function == "r":
	for i in range(initInfect):
		rid = random.choice(suceptible.keys())
		infected[rid] = suceptible[rid]
		del(suceptible[rid])
			
	
elif function == "a":
	repeateda = 0
	print(initInfect)
	for i in range(initInfect):
		rid = random.choice(suceptible.keys())
		repeated += infect(suceptible[rid])
			
#fraction = float(nInfected / n)

if len(infected.keys()) == n:
	print("It took " + str(t) + " days for " +
		str(f * 100) + "% of people to be infected with cost " + str(initInfect) + "and " + str(b) + " neighbours infected for day")
	
#print (fraction)
print("Infected: " + str(len(infected)))
print("Repeated Nodes " + str(repeated))
t = 1

while len(infected.keys()) + len(recovered.keys()) < 0.9 * n:
	inf = infected.keys()
	repeated = 0
	for i in inf:
		if infected[i].daysInfected == j:
			recovered[i] = infected[i]
			del(infected[i])
		else:
			if len(infected[i].edges) > 0:
				repeated += infect(infected[i])
				infected[i].daysInfected += 1

	nInfected = len(infected.keys()) + len(recovered.keys())
	#fraction = float(nInfected / n)
	#	print (fraction)
	print("Day: " + str(t))
	print("Infected: " + str(len(infected)))
	print("recovered: " + str(len(recovered)))
	print("Repeated Nodes " + str(repeated))
	t+=1

print("It took " + str(t) + " days for people to be infected with " + str(initInfect) + " nodes infected")
