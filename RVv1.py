#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def uni(x0):
    xi = 16807*x0%((2**31)-1)
    return xi

def triDist(lower = 0, upper = 1):
    U1 = np.random.uniform(lower,upper)
    U2 = np.random.uniform(lower,upper)
    return (U1+U2)/2
def normDist(mean = 0, std = 1):
    z1 = np.sqrt(-2*np.log(np.random.uniform(0,1)))*np.radians(np.cos(2*np.pi*np.random.uniform(0,1)))
    z2 = np.sqrt(-2*np.log(np.random.uniform(0,1)))*np.radians(np.sin(2*np.pi*np.random.uniform(0,1)))
    return z1

def recreationalVehicle(dist, kwargs):
    if dist == "triangular":
        return triDist(kwargs["lower"], kwargs["upper"])
    elif dist == "normal":
        return normDist(kwargs["mean"], kwargs["std"])
    elif dist == "bernoulli":
        return stats.bernoulli.ppf(np.random.random(), p = kwargs["p"])
    elif dist == "binomial":
        return stats.binom.ppf(np.random.random(),n = kwargs["n"], p = kwargs["p"])
    elif dist == "geometric":
        return stats.geom.ppf(np.random.random(), p = kwargs["p"])
    elif dist == "exponential":
        return stats.expon.ppf(np.random.random(), shape = 1/kwargs["lambda"])
    elif dist == "weibull":
        return stats.weibull_min.ppf(np.random.random(), c = kwargs["a"], scale = 1/kwargs["b"])
    elif dist == "gamma":
        return stats.gamma.ppf(np.random.random(), a = kwargs["a"], scale = 1/kwargs["b"])
    elif dist == "poisson":
        return stats.poisson.ppf(np.random.random(), mu = kwargs["mu"])
    elif dist == "erlang":
        return stats.erlang.ppf(np.random.random(), a = kwargs["a"], scale = 1/kwargs["b"])
    elif dist == "beta":
        return stats.beta.ppf(np.random.random(), a = kwargs["a"], b = kwargs["b"])
    elif dist == "crystalball":
        return stats.crystalball.ppf(np.random.random(), beta = kwargs["beta"], m = kwargs["m"])
    elif dist == "cauchy":
        return stats.cauchy.ppf(np.random.random())
    elif dist == "chi2":
        return stats.chi2.ppf(np.random.random(), df = kwargs["df"])



def RVConvoy(n, dist, kwargs):
    if dist == "uniform":
        xx = []
        x1 = []
        for i in range(n):
            if i == 0:
                xx.append(uni(np.random.randint(0,(2**31-1))))
            else:
                xx.append(uni(xx[i-1]))
            x1.append(xx[i]/((2**31)-1))
        return x1
    else:
        x = []
        for i in range(n):
            x.append(recreationalVehicle(dist, kwargs))
        return np.array(x)
def indiecheck(values):
    b = list(np.arange(0,1,0.2))
    counts, _, _ = plt.hist(values, bins=b)
    e = len(values)/5
    plt.close()
    oe = 0
    for i in counts:
        print(i, e)
        oe += (i-e)**2
    sigo = np.sum(oe)/e
    chisq = 7.815
    if sigo < chisq:
        return "approximatly uniform"
    else:
        return "not uniform"
def AReject(f, n, bounds = [0,1]):
    x = np.linspace(bounds[0], bounds[1], 1000)
    y = f(x)
    ymin = np.min(y)
    ymax = np.max(y)
    vals = []
    
    for i in range(n):
        eq = False
        while not eq:
            u1 = np.random.uniform(bounds[0], bounds[1])
            u2 = np.random.uniform(ymin,ymax)
            #print(u1, u2)
            if u2 <= f(u1):
                vals.append(u1)
                eq = True
    return vals

