[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)
```python
__author__ = 'martinrasumoff'

import nsfg
import numpy as np
import thinkplot
import thinkstats2


### Reading data into memory ###
df = nsfg.ReadFemPreg()

### Cleaning data in memory ###
df.is_copy = False
df = df[np.isfinite(df['totalwgt_lb'])]
df = df[np.isfinite(df['agepreg'])]

live = df

### Creating Scatterplot
thinkplot.Scatter(live['totalwgt_lb'], live['agepreg'])
thinkplot.Show(xlabel='Weight(lbs)',
               ylabel='Mother Age at End of Pregnancy (years)',
               axis=[0,17,10,50])

### Calculation of Pearson's and Spearman's Correlations
pearson = thinkstats2.Corr(live['totalwgt_lb'],live['agepreg'])
spearman = thinkstats2.SpearmanCorr(live['totalwgt_lb'],live['agepreg'])

print "      Pearson Correlation: "+str(pearson)
print "Spearman Rank Correlation: "+str(spearman)
```
