
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt



def readFile(file):
	f = open(file,'r')
	data = np.asarray(f.readlines(),dtype = 'float')
	f.close()
	return data
	
	
def plot_hist(file,label,subplot=111,xlim=None,ylim=None):
	data = readFile(file)
	plt.subplot(subplot)
	plt.hist(data,100,histtype='step',label=label)
	if xlim: plt.xlim(xlim)
	if ylim:plt.ylim(ylim)
	
	
	
	
	plt.xlabel('Charge (nC)')
	plt.ylabel('Counts')

def plot(x,f):
	plt.xlim([0.02,.1])
	plt.ylim([0,600])
	plt.xlabel('Charge (nC)')
	plt.ylabel('Counts')
	plt.plot(x,f)

plot_hist('redvals','100 N2',subplot=111,xlim = [0.02,.1],ylim = [0,600])
plot_hist('oxvals','80/20 N2/O2',subplot=111,xlim = [0.02,.1],ylim = [0,600])

# plt.subplot(212)
# plt.hist(readFile('monovals'),600,histtype='step',label='Monolithic')
# plt.xlim([0.1,0.4])

plt.legend()
plt.show()

# 
# red = readFile('redvals')
# h = np.histogram(red,bins=100)
# 
# x = np.linspace(h[1][0],h[1][-1],h[0].size)
# f = h[0]
# 
# 
# 
# 
# 
# plot(x,f)
# plt.show()

print (h[0].size,h[1].size)





