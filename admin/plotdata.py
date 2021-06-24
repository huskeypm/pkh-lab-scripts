#!/usr/bin/env python
import sys
##################################
#
# Revisions
#       10.08.10 inception
#
##################################

#
# ROUTINE  
#
"""
Plots data from brightview 
"""
import matplotlib.pylab as plt
import numpy as np
import re
  
def doit(days=30):
  
  allVals = dict()
  loc = "./"
  
  ## Get CPU
  lines = open(loc+'CPU', 'r').readlines() 
  lines = lines[:-1]   # omit the last line
  
  # get list
  vals =[]
  for line in lines:
    val = line.split()[2]
    vals.append(val) 
  
  allVals['CPU'] = np.asarray(vals,dtype=np.float)    
  
  
  ## GET GPU
  def reader(name):
      lines = open(name, 'r').readlines() 
      lines = lines[:-1]   # omit the last line
  
      # get list
      vals =[]
      for line in lines:
        val = line.split()[2]
        val = val.replace("%","") # rmv pct sign
        vals.append(val) 
  
      return np.asarray(vals,dtype=np.float) 
  
  gpuNames = []
  for i in range(4):
      name = "GPU%d"%i
      allVals[name] = reader(loc+name)
      gpuNames.append(name)
  
  # Date
  from datetime import datetime
  daDate = datetime.today().strftime('%Y-%m-%d')
  
  
  ### Plot datga 
  plt.bar(np.arange(days)-days,allVals['CPU'])
  plt.title("CPU Usage:\n One-minute load/Avg across 10 nodes: " + daDate)
  plt.xlabel("Days (from now)")
  plt.gcf().savefig("cpu.png") 
  
  
  ### plot GPU 
  plt.figure()
  tot=[]
  for gpu in gpuNames:
      tot.append( allVals[gpu] )
  tot=np.array(tot)
  avgGPU=np.mean(tot,axis=0)
  plt.bar(np.arange(days)-days,avgGPU,label="Average")#,alpha=0.1)
  
  for gpu in gpuNames:
      plt.bar(np.arange(days)-days,allVals[gpu],label=gpu,alpha=0.1)
  plt.legend()
  plt.title("GPU usage:\n " + daDate)
  plt.xlabel("Days (from now)")
  plt.gcf().savefig("gpu.png") 



#
# Message printed when program run without arguments 
#
def helpmsg():
  scriptName= sys.argv[0]
  msg="""
Purpose: 
 
Usage:
"""
  msg+="  %s -validation" % (scriptName)
  msg+="""
  
 
Notes:

"""
  return msg

#
# MAIN routine executed when launching this script from command line 
#
if __name__ == "__main__":
  import sys
  msg = helpmsg()
  remap = "none"

  if len(sys.argv) < 2:
      raise RuntimeError(msg)

  # Loops over each argument in the command line 
  for i,arg in enumerate(sys.argv):
    # calls 'doit' with the next argument following the argument '-validation'
    if(arg=="-run"):
      arg1=int( sys.argv[i+1] ) 
      doit(arg1)
      quit()
  





  raise RuntimeError("Arguments not understood")




