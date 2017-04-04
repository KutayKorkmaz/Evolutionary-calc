import random
import numpy as np
import operator
TEMP=270
L=174
R=273
Datas=[]

def temperature (OL,OR,GL,GR):
	tempr = (L+OL)*GL + (R+OR)*GR
	return tempr

def create_mutant (List1,List2):
	OL=float(List1[0]+List2[0])/2
	OR=float(List1[1]+List2[1])/2
	GL=float(List1[2]+List2[2])/2
	Gr=float(List1[3]+List2[3])/2
	tempr=temperature(OL,OR,GL,GR)
	remain=abs(tempr-TEMP)	
	mutant= (OL,OR,GL,GR,remain)
	return mutant

 
for j in range(10):
	OL=random.randint(-25,25)
	OR=random.randint(-25,25)
	GL=float(random.randint(1,19))/10
	GR=float(random.randint(1,19))/10
	tempr=temperature(OL,OR,GL,GR)
	remain=abs(tempr-TEMP)
	Datas.append((OL,OR,GL,GR,remain))

print "Initial data"
for j in range(len(Datas)):
	print j, Datas[j]


while 1:
	Datas.sort(key=operator.itemgetter(4))
	if Datas[0][4]<1:
		print "\n\n******RESULT*******"
		print Datas[0]
		exit()
	print '************************************************'
	print "Sorted initial data"
	for j in range(len(Datas)):
		print j, Datas[j]
	Datas=Datas[:5]#Delete last 5
	print '************************************************'
	print "Survived data"
	for j in range(len(Datas)):
		print j, Datas[j]

	Datas.append(create_mutant(Datas[0],Datas[1]))
	Datas.append(create_mutant(Datas[0],Datas[2]))
	Datas.append(create_mutant(Datas[1],Datas[2]))
	for j in range(3):
		OL=random.randint(-25,25)
		OR=random.randint(-25,25)
		GL=float(random.randint(1,19))/10
		GR=float(random.randint(1,19))/10
		tempr=temperature(OL,OR,GL,GR)
		remain=abs(tempr-TEMP)
		Datas.append((OL,OR,GL,GR,remain))

	print '************************************************'
	print "Survived+Mutation data+Rew_rand"
	for j in range(len(Datas)):
		print j, Datas[j]



