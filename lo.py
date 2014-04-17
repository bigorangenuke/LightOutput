
import numpy as np
import scipy.signal as sg
import scipy.optimize as so
from matplotlib import pyplot as plt
import jmath as jm
from scipy.stats import kde

from scipy.stats import norm


def readFile(file):
	f = open(file,'r')
	data = np.asarray(f.readlines(),dtype = 'float')
	f.close()
	return data
	
	
def plot_hist(file,**kwargs):
	bins = 100
	label = None
	subplot = 111
	xlim = None
	ylim = None
	markers = None
	
	if 'bins' in kwargs:
		bins = kwargs['bins']
	if 'label'in kwargs:
		label = kwargs['label']
	if 'subplot' in kwargs:
		subplot = kwargs['subplot']
	if 'xlim' in kwargs:
		xlim = kwargs['xlim']
	if 'ylim' in kwargs:
		ylim = kwargs['ylim']
	if 'markers' in kwargs:
		markers = kwargs['markers']
	
	data = readFile(file)
	plt.subplot(subplot)
	plt.hist(data,bins,histtype='step',label=label)
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

# plot_hist('redvals',label = '100 N2',subplot=111,xlim = [0.02,.1],ylim = [0,600])
# plot_hist('oxvals',label = '80/20 N2/O2',subplot=111,xlim = [0.02,.1],ylim = [0,600])
# plt.title('Li Glass, 200 um rods, Quasi-thermal Neutrons, -1480 V')
# # plt.subplot(212)
# # plt.hist(readFile('monovals'),600,histtype='step',label='Monolithic')
# # plt.xlim([0.1,0.4])
# 
# plt.legend()
# plt.show()



#gaussian function
def gauss(x,*p):
	A,mu,sigma = p
# 	print(p)
# 	print(len(p))
	g = A*np.exp(-(x-mu)**2/(2.*sigma**2))
# 	print(g.size)
	#plt.plot(bin_centers,hist)
	return g


def fit(file):
	data = readFile(file)

	hist,bin_edges=np.histogram(data,bins=100)
	bin_centers=(bin_edges[:-1]+bin_edges[1:])/2.
	
	s1 = 66
	s2 = 90
	hist= hist[s1:s2]
	bin_centers = bin_centers[s1:s2]
	plt.plot(bin_centers,hist)
	plt.show()
	p0 = [500.,0.1,0.05]
	coeff, var_matrix=so.curve_fit(gauss,bin_centers,hist,p0=p0)
	x = np.linspace(np.min(bin_centers),np.max(bin_centers),1000)
	hist_fit = gauss(x,*coeff)
	#g = gauss(x,50000,0.25,0.25)
	plt.plot(x,hist_fit,label='fit',c='r')
	plt.plot(bin_centers,hist,label='data',marker = 'o')
	
	print (coeff)
	print ('mu = %s\t sigma = %s'%(coeff[1],coeff[2]))
	return coeff

#plot_hist('monovals',label = 'data',bins=500,xlim=[0,0.4],ylim=[0,60000],markers='o')
plt.title('Li Glass, Glass Rods,Quasi-thermal Neutrons, -1480 V')
#fit('monovals')
plt.legend()
#plt.show()

fit('redvals')
plt.show()
#fit('monovals')

