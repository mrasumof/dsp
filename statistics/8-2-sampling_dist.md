[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)
```python
__author__ = 'martinrasumoff'

import numpy as np
import thinkstats2
import math
import thinkplot

def MeanError(estimates, actual):
    """Computes the mean error of a sequence of estimates.

    estimate: sequence of numbers
    actual: actual value

    returns: float mean error
    """
    errors = [estimate-actual for estimate in estimates]
    return np.mean(errors)


def RMSE(estimates, actual):
    """Computes the root mean squared error of a sequence of estimates.

    estimate: sequence of numbers
    actual: actual value

    returns: float RMSE
    """
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)

lam = 2

means = []

for i in range(1000):
    xs = np.random.exponential(1.0/lam,10)
    L = 1 / np.mean(xs)
    means.append(L)

cdf = thinkstats2.MakeCdfFromList(means)
ci = cdf.Percentile(5), cdf.Percentile(95)

print "RMSE L:",RMSE(means,lam)
print "Mean error L:",MeanError(means,lam)
print "90% Confidence Interval: "+str(ci)
```
