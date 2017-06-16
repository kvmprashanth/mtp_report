import numpy as np

data = np.loadtxt("../plot.data",skiprows=0)
#data = data/1048576

fw = open("../dist_ma.data", "w+")

olda1 = 0
olda2 = 0

for i in range(len(data[:,8])):
    line = str(i)+"\t"+str(data[i,8]-olda1)+ "\t"+ str(data[i,9]-olda2) + "\n"
    fw.write(line)
    olda1 = data[i, 8]
    olda2 = data[i, 9]



