import random as rd
import matplotlib.pyplot as pp

def step(b):
	return(b + rd.uniform(-1,1))

iterations = 100
walkers = 1

x = [0]
list = [0]

xml = [0]
xmsl = [0]

xt = 0
xst = 0

xm = 0
xms = 0

pp.axis((-1,100,-5,5))

for i in range (walkers):
	x = [0]
	list = [0]
	xml = [0]
	xmsl = [0]
	for j in range (iterations):
		x.append(j)
		list.append(step(-1))
		xt = 0
		xst = 0
		for k in range(len(x)):
			xt += (list[k])
			xst += (list[k]**2)
		xm = xt/len(list)
		xms = xst/len(list)
		
		xml.append(xm)
		xmsl.append(xms)
	pp.plot(x,xml,'b-')	
	pp.plot(x,xmsl,'r-')	


pp.show()
