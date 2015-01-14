"""
temp2 = nodesCat

for i in range(22):
	nodesCat = temp2
	done = []
	while len(nodesCat) > 0:
		for node in nodesCat:
			if node not in done:
				done.append(node)
				for link in outlinks[node]:
					if link not in done:
						x = int(nodesCat[node][i]) - 2
						if x > 0:
							nodes[link][i] = x
							temp[link] = blank
							temp[link][i] = x
							count = count + 1
				for link in inlinks[node]:
					if link not in done:
						x = int(nodesCat[node][i]) - 3
						if x > 0:
							nodes[link][i] = x
							temp[link] = blank
							temp[link][i] = x
							count = count + 1
		nodesCat = temp
		temp = {}
"""	

"""

 # percolate through graph using shallow algorithm
temp2 = nodesCat
for i in range(22):
	nodesCat = temp2
	done = []
	while len(nodesCat) > 0:
		for node in nodesCat:
			if node not in done:
				done.append(node)
				for link in outlinks[node]:
					if link not in done:
						x = int(nodesCat[node][i]) - 2
						if x > 0:
							nodes[link][i] = x
							temp[link] = blank
							temp[link][i] = x
							count = count + 1
				for link in inlinks[node]:
					if link not in done:
						x = int(nodesCat[node][i]) - 3
						if x > 0:
							nodes[link][i] = x
							temp[link] = blank
							temp[link][i] = x
							count = count + 1
		nodesCat = temp
		temp = {}	


 #percolate using third algorithm
for i in range(22):
	for node in nodes:
		x = int(nodes[node][i])
		if x > 0:
			for link in outlinks[node]:
				nodes[link][i] = int(nodes[link][i]) + max(0, x - 2)
			for link in inlinks[node]:
				nodes[link][i] = int(nodes[link][i]) + max(0, x - 3)
"""