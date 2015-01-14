nodes = []

f = open("nodes.csv", "r")
x = 'notempty'
while x != "":
	x = f.readline()
	y = x.strip()
	y = y + ",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
	nodes.append(y)
f.close()

f = open('nodesInit.csv','w')
for x in nodes:
	f.write(x + '\n')
f.close()