#!/usr/bin/python
from time import sleep 
import commands, psutil, sys

# Number of Containers
n = 4

# Initializations
c_name = ['m1', 'm2', 'r1', 'r2']
c = []
line = ""
count = 1

# File handlers
f_sr = [] 
f_sl = []
f_usage = []

# File read values
sl = []
sr = []
usage = []

#initialize file for writing
f_data = open("/home/prashanth/Workspace/mem_reclamation/experiments/plotter/collected.dat", "w")

# Initializing file handlers for each container
for i in range(n):
        cmd = 'docker ps -aqf "name=%s" --no-trunc'%(c_name[i])
        c.append(commands.getstatusoutput(cmd)[1])
        container_path = "/sys/fs/cgroup/memory/docker/"+c[i]
        
        f_sr.append(open(container_path+"/memory.soft_reclaimed", "w+"))
	f_sr[i].write("0")
	sr.append("0")
        
        f_sl.append(open(container_path+"/memory.soft_limit_in_bytes", "r"))
        sl.append(f_sl[i].read().strip())
                
        f_usage.append(open(container_path+"/memory.usage_in_bytes", "r"))
        usage.append("0")

while 1:
   
        # Read SR and Usage for each container
        for i in range(n):
                try:
                        f_sr[i].seek(0)
                        sr[i] = f_sr[i].read().strip()
                except:
                        if i == n-1:
                                print "Collector Terminated"
                                sys.exit()
                                
                        
                try:
                        f_usage[i].seek(0)
                        usage[i] = f_usage[i].read().strip()
                except:
                        usage[i] = 0      

        # Reading System Memory
        sysmem = psutil.virtual_memory()
              
        # Output Lines
        line = str(count)
        for i in range(n):
                line += "\t" + str(usage[i]) + "\t" + str(sl[i]) + "\t" + str(sr[i]) 
        #line += "\t" + str(mpusage) + "\t" + str(sysmem.free) + "\n"
        line += "\t" + str(sysmem.free) + "\n"
        f_data.write(line)

        count += 1
        sleep(1)
    
print("Collector has terminated")
