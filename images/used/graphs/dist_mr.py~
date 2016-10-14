import numpy as np

data = np.loadtxt("../plot.data",skiprows=0)
#data = data/1048576

fw = open("../dist_mr.data", "w+")

olda1 = 0
olda2 = 0

for i in range(len(data[:,1])):
    line = str(i)+"\t"+str(data[i,1]-olda1)+ "\t"+ str(data[i,2]-olda2) + "\n"
    fw.write(line)
    olda1 = data[i, 1]
    olda2 = data[i, 2]



