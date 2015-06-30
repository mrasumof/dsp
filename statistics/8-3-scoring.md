# 4) Think Stats Exercise 8.3

Problem: [Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)
```python
__author__ = 'martinrasumoff'

import random

lam = 0.025

score = []
time = 0
goal = 0

goal = int(random.expovariate(lam))
time = time + goal

while (time <= 90):
    score.append(time)
    goal = int(random.expovariate(lam))
    time = time+goal

print "Team Scored        : "+str(len(score))+" goals"
print "Scored at (minutes): "+str(score)
```
