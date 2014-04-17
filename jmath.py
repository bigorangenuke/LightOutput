import numpy as np
import scipy.signal as sp
def exp(x,a,b,c):
    return a*np.exp(b*x)+c

# def gaussian(n,a,b,c,d):
#     f = []
#     x=[]
#     for xx in range(-n/2,n/2):
#         xx*=0.1
#         ff = a*np.exp(-(xx-b)*(xx-b)/(2*c*c))+d
#         x.append(xx)
#         f.append(ff)
#     return np.array(x),np.array(f)
def mode(a, axis=0):
    scores = np.unique(np.ravel(a))       # get ALL unique values
    testshape = list(a.shape)
    testshape[axis] = 1
    oldmostfreq = np.zeros(testshape)
    oldcounts = np.zeros(testshape)

    for score in scores:
        template = (a == score)
        counts = np.expand_dims(np.sum(template, axis),axis)
        mostfrequent = np.where(counts > oldcounts, score, oldmostfreq)
        oldcounts = np.maximum(counts, oldcounts)
        oldmostfreq = mostfrequent
        
    return mostfrequent, oldcounts

def findzeros(x,ff):
    z=[]
    if not isinstance(ff,list):
        for i,d in enumerate(ff):
            if np.sign(d)!=np.sign(ff[i-1]):
                z.append([i,x[i],d])
                #print [i,d]      
    else:
        for j,f in enumerate(ff):

            for i,d in enumerate(f):
                if np.sign(d)!=np.sign(f[i-1]):
                    z.append([j,i,x[i],d])
                    #print j,[i,x[i],d]
    return z

def findpeaks(x,f):  
    #print sp.find_peaks_cwt(f)
    mx = np.argmax(f)
    mn = np.argmin(f)
    
    print(mx-mn)
   
def testForNoise(f): 
    mx = np.argmax(f)
    mn = np.argmin(f)
 
    print ('testfornoise')
    if mx-mn<61:
        print(mx-mn)
        return True
    
    return False
def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]   
def gaussian(sigma,mu,**kwargs):

    size = 1000
    derivatives = 0
    bounds = [-3*sigma,3*sigma]
    only=False
    if 'size' in kwargs:
        size = kwargs['size']
    if 'derivatives' in kwargs:
        derivatives=kwargs['derivatives']
    if 'bounds' in kwargs:
        bounds=kwargs['bounds']
    if 'only' in kwargs:
        only = kwargs['only']

    
    x = np.linspace(bounds[0], bounds[1], size)
    
    out = []
    
    if only:
        if derivatives==0:
            f = 1./sigma/np.sqrt(2*np.pi)*np.exp(-(x-mu)*(x-mu)/(2*sigma*sigma))
            return x,f
        if derivatives==1:
            df= (x-mu)**3/(sigma**3)/np.sqrt(2*np.pi)*np.exp(-(x-mu)*(x-mu)/(2*sigma*sigma))
            return x,df    
        if derivatives==2:
            ddf = 1/np.sqrt(np.pi*2)*sigma**5*(-sigma**2+x**2)*np.exp(-x*x/(2*sigma*sigma))
            return x,ddf
            
    
    
    f = 1./sigma/np.sqrt(2*np.pi)*np.exp(-(x-mu)*(x-mu)/(2*sigma*sigma))
    out.append(f)
    
    if derivatives==1:
        df = (x-mu)**3/(sigma**3)/np.sqrt(2*np.pi)*np.exp(-(x-mu)*(x-mu)/(2*sigma*sigma)) 
        out.append(df)
    elif derivatives==2:
        df = (x-mu)**3/(sigma**3)/np.sqrt(2*np.pi)*np.exp(-(x-mu)*(x-mu)/(2*sigma*sigma)) 
        #ddf = (2*(x-mu)**3+3*(x-mu)**2)*np.exp(-(x-mu)**2/(2*sigma**2))/(sigma**3*np.sqrt(2*np.pi))
        #ddf = np.exp((mu-x)**2/(2*sigma**2))*((mu-x)**2-sigma**2)/(np.sqrt(2*np.pi)*sigma**3)
        ddf = 1/np.sqrt(np.pi*2)*sigma**5*(-sigma**2+x**2)*np.exp(-x*x/(2*sigma*sigma))
    
        out.append(df)
        out.append(ddf)

    return x,out


def convolve(data,kernel,**kwargs):
    normalize=False
    if 'normalize' in kwargs:
        normalize = kwargs['normalize']
    c = np.convolve(data,kernel,'same')
    if normalize:c/=np.sum(c)
    return c








