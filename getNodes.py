f = open('nodes.json','r')

nodes = []

x = 'notempty'

while x != '':
	x = f.readline()
	if 'id:' in x:
		x = x.strip()
		x = x.split(':')[1]
		nodes.append(x)
f.close()

f = open('nodes.csv','w')
for x in nodes:
	f.write(x + '\n')
f.close()