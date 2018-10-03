#!/usr/bin/env python
# coding: utf-8

# ## Problem 1
# 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.
# 
# ### Approach
# 
# in mod15, the multiples of 3 and 5 will always be 3, 5, 6, 9, 10, 12, 15. the sum of these numbers is 60.

# And there are 7 of these elements. So between every multiple of 15 (meaning the ranges [1-15], [16-30], etc), the sum will be $60 + (7*m)$ where $m$ is the multiple of 15 beginning the range.
# 
# Then, for $n$ multiples of 15, we have
# 
# $$\sum_{i=0}^{n-1} (60 + 105i)$$
# 
# then, for the remainder, you can just iterate through and add the leftovers, so if you're looking for less than 1000, you'd divide, find the highest multiple is 990, and then manually check for multiples between 991 and 999.

# In[1]:


import numpy as np;
import math;


# In[2]:


print(3 + 5 + 6 + 9 + 10 + 12 + 15)


# In[30]:


limit=1000
multiples=limit//15;
lastmult=(multiples*15);

"there are {0} multiples of 15, the highest being {1}".format(
    multiples, lastmult)


# In[21]:


x_mod = [60 + 105*i for i in range(1,10)]

# Turns out range is inclusive/exclusive, meaning range(1,10) is
# the interval [1,10). I didn't know this. So there will be end-start
# values in the range
x_mod


# In[5]:


intvlsum = lambda i: 60 + 105*i;
print (type(intvlsum))
print (intvlsum(4))


# In[12]:


print ("Sum: %d" % sum( intvlsum(x) for x in range(0,9) ))


# In[19]:


total=sum( intvlsum(x) for x in range(0,multiples) )
print ("Before leftovers: %d" % total)

# last multiple + 1 because the last multiple (990 if limit is 1000)
# is counted by the last interval sum, since I am using the intervals
# ending in the previous multiple. This probably would be cleaner if I
# just had the multiple *start* the interval instead.
for n in range(lastmult+1, limit):
    if (n % 3 == 0 or n % 5 == 0):
        print ("%d is a remaining multiple" % n)
        total += n;
        
print (total)

