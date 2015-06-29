[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)
```python
### Exercise 2.4 ###

import numpy
import nsfg
import thinkstats2
import numpy as np
import math
 
### Reading data into memory ###\
df = nsfg.ReadFemPreg()

### Cleaning data in memory ###
df.is_copy = False

na_vals = [97, 98, 99]

live = df

live.birthwgt_lb.replace(na_vals, np.nan, inplace=True)
live.birthwgt_oz.replace(na_vals, np.nan, inplace=True)

### Adding a new column with the sum of lbs and oz ###
live['totalwgt_lb'] = df.birthwgt_lb + df.birthwgt_oz / 16.0

### Differentiating first childs vs. others ###
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

### Performing Calculations\
firsts_mean = firsts.totalwgt_lb.mean()
firsts_var = firsts.totalwgt_lb.var()
firsts_std = firsts.totalwgt_lb.std()

others_mean = others.totalwgt_lb.mean()
others_var = others.totalwgt_lb.var()
others_std = others.totalwgt_lb.std()

print '\n\nFirst Babies Total Weight Mean =',firsts_mean
print '                          Var  =',firsts_var
print '                          Std  =', firsts_std

print 'Other Babies Total Weight Mean =', others_mean
print '                          Var  =',others_var
print '                          Std  =',others_std

### Calculating Cohen\'92s Effect Size ###\
n1 = len(firsts)
n2 = len(others)

diff = firsts.totalwgt_lb.mean() - others.totalwgt_lb.mean()
pooled_var = (n1 * firsts_var + n2 * others_var) / (n1+n2)

CohenEffectSize = diff/math.sqrt(pooled_var)
print "\n\nCohen's Effect Size: " + str(CohenEffectSize)
```
