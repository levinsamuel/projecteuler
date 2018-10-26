#!/usr/bin/env python
# coding: utf-8

# # Workspace for Project Euler problems
# 
# ## Problem 10
# 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

# In[1]:


import tools.primetools as pt
import numbers, math
import tools.misc as misc
import logging, sys
from functools import reduce

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

log = logging.getLogger("main")

# DEBUG, INFO, WARNING, ERROR, CRITICAL
log.setLevel(logging.DEBUG)


# In[2]:


dir(pt)


# In[3]:


help(pt.factor)
help(pt.findSomePrimes)
help(pt.smallestCommonMultiple)


# In[4]:


# pt.log.setLevel(logging.DEBUG)
below2M=pt.findSomePrimes(limit=2000000)
len(below2M)


# In[5]:


sumofprimes=reduce(lambda x,y:x+y, below2M.keys())

print(f"Sum of primes below 2M: {sumofprimes}")
print(f"Highest prime: {max(below2M.keys())}")

