import scipy as sp
import matplotlib.pyplot as plt
import numpy as np

def error(f,x,y):
    return np.sum((f(x)-y)**2)
data = sp.genfromtxt("data.tsv", delimiter="\t")
x = data[:,0]
y = data[:,1]
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]


plt.scatter(x,y, s=10)
plt.title("Web traffic over the last month")
plt.xlabel("time-axis")
plt.ylabel("hits/hour")
plt.xticks([w*7*24 for w in range(10)],['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid(True, linestyle='-', color='0.75')

#to find the underlying model and relatioinship of data order 1
fp1, residuals, rank, sv, rcond = np.polyfit(x,y,1,full=True)
f1 = np.poly1d(fp1)
fx = np.linspace(0,x[-1],1000)
plt.plot(fx, f1(fx), linewidth=4)

#plt.show()
#order 2
f2p = np.polyfit(x,y,10)
f2 = np.poly1d(f2p)
error2 = error(f2,x,y)

plt.plot(fx, f2(fx), 'r--')
plt.legend(["d=%i"%f1.order,"d=%i"%f2.order], loc="uppper left")
plt.show()
