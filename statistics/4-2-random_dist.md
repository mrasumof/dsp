[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)
```python
__author__ = 'martinrasumoff'

import matplotlib
import chap01soln
import thinkstats2
import thinkplot
import random

pmf = {}
cdf = {}

freq = [0,0,0,0,0]

for a in range(1000):
    i = random.random()
    if i >= 0 and i < 0.2:
        freq[0] = freq[0]+1
    elif i >= 0.2 and i < 0.4:
        freq[1] = freq[1] + 1
    elif i >= 0.4 and i <= 0.6:
        freq[2] = freq[2] + 1
    elif i >= 0.6 and i <= 0.8:
        freq[3] = freq[3] + 1
    else:
        freq[4] = freq[4] + 1

pmf_list = { 0: freq[0], 1: freq[1], 2: freq[2], 3: freq[3], 4: freq[4]}
pmf = thinkstats2.Pmf(pmf_list,label="PMF")
pmf.Normalize()
cdf = thinkstats2.Cdf(pmf,label="CDF")


thinkplot.PrePlot(1)
thinkplot.Pmfs([pmf])
thinkplot.Show(xlabel="Number",ylabel="PMF")

thinkplot.PrePlot(1)
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel="Number",ylabel="CDF")
```
