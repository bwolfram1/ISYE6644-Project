#%%
import RVv1
import matplotlib.pyplot as plt
import numpy as np
def fun(x):
    return (x**2)*3

x = RVv1.RVConvoy(10000, "weibull", {"a": 1.95, "b": 2})
plt.hist(x, bins=15)
plt.title("Weibull distribution from inverse transform")
plt.show()


x1 = np.linspace(0,1,1000)
y1 = fun(x1)

v = RVv1.AReject(fun,10000)
#print(v)
plt.plot(x1,y1)
plt.hist(v,density=True)
plt.title("Accetpted Rejection Distribution")
plt.show()

#x = RVConvoy(5, "weibull", {"a": 1.95, "b": 2})
#u = RVConvoy(10000, "uniform", {})
#for i in range(10000):
    #xx.append(stats.weibull_min.ppf(np.random.random(), scale=0.5, c=1.95))
#print(x)
#def fun(x):
#    return (x**2)*3
#print(normDist(1,1))
#x1 = np.linspace(0,1,1000)
#y1 = fun(x1)

#v = AReject(fun,5)
#print(v)
#plt.plot(x1,y1)
#plt.hist(v,density=True)
#plt.show()
#print(indiecheck(u))
#plt.hist(x, bins=10)
#plt.show()