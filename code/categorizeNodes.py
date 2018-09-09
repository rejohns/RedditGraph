import random

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

nodes = {}
nodesCat = {}

f = open("nodesInit.csv", "r")
x = 'notempty'
while x != "":
	x = f.readline()
	y = x.strip()
	y = y.split(",")
	nodes[y[0]] = y[1:23]
f.close()

inn = ""
while inn != "q":
	sub = random.choice(nodes.keys())
	bad = True
	while bad:
		print sub
		inn = raw_input(">>> ").strip().split()
		if len(inn) == 1:
			if inn[0] == "q":
				inn = "q"
				bad = False
			elif inn[0] == "n":
				inn = "n"
				bad = False
		elif len(inn) == 2:
			if inn[0] in categories and inn[1] in ["0","1","2","3"]:
				dex = categories.index(inn[0])
				nodesCat[sub] = nodes[sub]
				nodesCat[sub][dex] = int(inn[1]) * 3

f = open('nodesCat.csv','a')
for x in nodesCat:
	y = ",".join(str(z) for z in nodes[x])
	if x + "," + y + "\n" != ",":
		f.write(x + "," + y + "\n")
f.close()