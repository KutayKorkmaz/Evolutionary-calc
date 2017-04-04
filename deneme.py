import random
import numpy as np
import operator
TEMP=270
L=174
R=273
Datas=[]
def temperature (offl,offr,lgain,gainr):
	TEMPe=(L+offl)*lgain+(R+offr)*gainr
	return TEMPe
 
for j in range(10):
	OL=random.randint(-25,25)
	OR=random.randint(-25,25)
	LG=random.uniform(0.1,1.9)
	GR=random.uniform(0.1,1.9)
	tempr=temperature(OL,OR,LG,GR)
	remain=abs(tempr-TEMP)
	Datas.append((OL,OR,LG,GR,remain))
print Datas
Datas.sort(key=operator.itemgetter(4))
print '************************************************'
print Datas
