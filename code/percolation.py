import copy

categories = [\
        "movies",\
        "tv",\
        "music",\
        "art",\
        "lit",\
        "food",\
        "games",\
        "tech",\
        "science",\
        "meta",\
        "sports",\
        "local",\
        "life",\
        "sex",\
        "gay",\
        "news",\
        "politics",\
        "history",\
        "religion",\
        "comedy",\
        "animals",\
        "nature"
        ]
blank = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
nodes = {}
edges = []
nodesCat = {}
outlinks = {}
inlinks  = {}
temp = {}
temp2 = {}

 # get node vector
f = open('nodesInit.csv','r')
x = 'notempty'
while x != "":
	x = f.readline()
	if x != '':
		y = x.strip().split(',')
		for i in range(23):
			if i != 0:
				y[i] = int(y[i])	
				nodes[y[0]] = y[1:23]	
				outlinks[y[0]] = []
				inlinks[y[0]] = []
f.close()

numNodes = len(nodes)
	
 # get initial categorized node vector
f = open("nodesCat.csv", "r")
x = 'notempty'
while x != "":
	x = f.readline()
	if x != '':
		y = x.strip().split(",")
		for i in range(23):
			if i != 0:
				y[i] = int(y[i])
				nodes[y[0]] = y[1:23]
				nodesCat[y[0]] = y[1:23]
f.close()	
		
 # get adjacency data and update dictionaries
f = open('edges.csv','r')
x = 'notempty'
numEdges = 0
while x != "":
	x = f.readline()
	if x != "":
		numEdges = numEdges + 1
		x = x.strip()
		x = x.split(',')
		edges.append([x[0],x[1]])
		outlinks[x[0]].append(x[1])
		inlinks[x[1]].append(x[0])
f.close()

count = len(nodesCat)

#"""
 # percolate through list using deep algorithm
for i in range(22):
	changed = nodesCat
	next = {}
	last = {}
	# change to 1 for faster with fewer results
	for iteration in [1,2]:
		for node in changed:
			for link in outlinks[node]:
				if link not in last:
					x = nodes[node][i] + int(nodes[node][i]) - 2
					if x > 0:
						nodes[link][i] = x
						next[link] = nodes[link]
						count = count + 1
			for link in inlinks[node]:
				if link not in last:
					x = nodes[node][i] + int(nodes[node][i]) - 3
					if x > 0:
						nodes[link][i] = x
						next[link] = nodes[link]
						count = count + 1
		last = copy.deepcopy(changed)
		changed = copy.deepcopy(next)					
			

 # set primary dictionary
graph = {}
for node in nodes:
	graph[node] = 0
	maxx = 0
	for i in nodes[node]:
		if i > maxx:
			maxx = i
			graph[node] = nodes[node].index(maxx)
	if maxx == 0:
		graph[node] = -1

 # write node list to .gdf file
f = open('graph.gdf','w')
f.write("nodedef>name VARCHAR, label VARCHAR, primary INT,")
for i in categories:
	if i != "nature":
		f.write(i + " BOOLEAN,")
	else:
		f.write(i + " BOOLEAN\n")
for i in graph:
	f.write(i + "," + i + "," + str(graph[i]) + ",")
	for j in range(22):
		if j != 21:
			f.write(str(nodes[i][j] > 0) + ",")
		else:
			f.write(str(nodes[i][j] > 0) + "\n")
f.write("edgedef>node1 VARCHAR,node2 VARCHAR,directed BOOLEAN\n")
for i in edges:
	f.write(i[0]+ "," + i[1] + ",true\n")
f.close()
			