#!/usr/bin/env python
# coding: utf-8

# # Workspace for Project Euler problems
# 
# ## Problem 13
# 
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# 
# _Number is below_

# In[1]:


import primetools as pt
import numbers, math
import tools.misc as misc
import logging, sys, time
from functools import reduce

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

log = logging.getLogger("main")

# DEBUG, INFO, WARNING, ERROR, CRITICAL
log.setLevel(logging.INFO)


# In[10]:


with open('problem13_number.txt', 'r') as f:
    num=f.read();
    
nums=num.split()
print (len(nums))
first10=nums[0][0:10]
print(first10)


# In[12]:


# does this fail?
print (int(nums[0]))
# no? this?
nums=[int(n) for n in nums]


# In[13]:


sm=sum(nums)
print(sm)


# In[ ]:




