[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)
```
__author__ = 'martinrasumoff'

import matplotlib
import scipy.stats

perc_men_low_end = scipy.stats.norm.cdf(177.8,loc=178,scale=7.7)
perc_men_high_end = scipy.stats.norm.cdf(185.42,loc=178,scale=7.7)

print perc_men_low_end
print perc_men_high_end
print "\n"

total_men = perc_men_high_end - perc_men_low_end
print str(total_men * 100) + "%"
```
