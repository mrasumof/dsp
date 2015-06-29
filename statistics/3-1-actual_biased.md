[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)
```python
__author__ = 'martinrasumoff'

import matplotlib
import chap01soln
import thinkstats2
import thinkplot

resp = chap01soln.ReadFemResp()


number_kids = resp.numkdhh
pmf = thinkstats2.Pmf(number_kids,label="Actual")

new_pmf = pmf.Copy(label="New Pmf")

for x, p in pmf.Items():
    new_pmf.Mult(x, x)

new_pmf.Normalize()

print 'Mean DB Mean: '+str(pmf.Mean())
print 'New PMF Mean: '+str(new_pmf.Mean())

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf,new_pmf])
thinkplot.Show(xlabel="Number of Kids",ylabel="PMF")
```
