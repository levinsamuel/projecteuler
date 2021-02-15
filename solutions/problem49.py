#!/usr/bin/env python
# coding: utf-8

# # Workspace for Project Euler problems
# 
# ## Problem 49

# In[1]:


import tools.primetools as pt
import numbers, math
import tools.misc as misc
import logging, sys, time
from functools import reduce

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

log = logging.getLogger("main")

# DEBUG, INFO, WARNING, ERROR, CRITICAL
log.setLevel(logging.INFO)


# In[2]:


primes = pt.findSomePrimes(limit=10000)


# In[4]:


ps = set(p for p in primes if p > 1000)


# In[10]:


sorted("1324")


# In[17]:


def find_prime_anagrams():
    solutions = []
    for p in ps:
    #     print(p)   
        limit = p + (10000 - p)//2
        pl = sorted(str(p))
        for next_num in range(p + 18, limit, 18):
    #         print(next_num)
            if next_num in ps and pl == sorted(str(next_num)):
    #             print("found a candidate:", next_num)
                dif = next_num - p
                last_num = next_num + dif
                if last_num in ps and pl == sorted(str(last_num)):
#                     print("winner", p, next_num, last_num)
                    solutions.append((p, next_num, last_num))
    #     break
    return solutions


# In[18]:


get_ipython().run_line_magic('timeit', 'find_prime_anagrams()')

