import numpy as np

data = np.loadtxt("../plot.data",skiprows=0)
#data = data/1048576

fw = open("../additional_mr.data", "w+")

olda1 = 0
olda2 = 0

for i in range(len(data[:,1])):
    
    exceed = (data[i,1]-olda1) - (data[i,2]-olda2)
    
    if exceed >= 0: 
        line = str(i)+"\t"+str(exceed)+ "\t"+ "0" + "\n"
    else:
        line = str(i)+"\t"+"0"+ "\t"+ str(-exceed) + "\n"
    
    fw.write(line)
    olda1 = data[i, 1]
    olda2 = data[i, 2]

