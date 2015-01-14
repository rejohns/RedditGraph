f = open('edges.json','r')

inn = []
out = []

x = 'nottempty'

while x != '':
	x = f.readline()
	if 'source:' in x:
		x = x.strip()
		x = x.split(':')[1]
		inn.append(x)
	elif 'target:' in x:
		x = x.strip()
		x = x.split(':')[1]
		out.append(x)
f.close()

f = open('data.csv','w')
i = 0
for x in inn:
	f.write(x + ',' + out[i] + '\n')
	i += 1
f.close()