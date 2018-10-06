#!/usr/bin/env python
# coding: utf-8

# # Workspace for Project Euler problems
# 
# ## Problem 3
# 
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143?

# ### Approach
# 
# If I'm not mistaken, there isn't a good algorithm to efficiently factor numbers. Maybe there are ways to parallelize and take advantage of different hardware, but not to avoid the basic method of checking.
# 
# It would be helpful to have a list of prime numbers here, rather than having to figure out which numbers are prime.
# 
# One thing we can do is, if this number has any prime factors larger than its square root, it will have at most one, since the product of two factors larger than its square root will be larger than the number itself. So we can check only factors up to its square root and we'll either find the largest one that way or whatever number is left will be its largest factor.

# In[34]:


import math
import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.INFO)

log = logging.getLogger("main")

# DEBUG, INFO, WARNING, ERROR, CRITICAL
log.setLevel(logging.DEBUG)

ournum=600851475143


# In[35]:



factored=ournum

oursqrt=math.ceil(math.sqrt(ournum))
oursqrt

largestprime=1
primes=[]
for i in range(2, oursqrt):
    f=factored/i
    while f.is_integer():
        log.debug('f={0} is integer. i={1} divides it'.format(f,i))
        factored=f
        largestprime=i
        primes.append(i)
        f=factored/i


# In[36]:


primes


# In[43]:


if factored == 1:
    # largest prime is already assigned
    log.debug('factored is 1')
else:
    largestprime=factored;

print ('largest prime: ', largestprime)

