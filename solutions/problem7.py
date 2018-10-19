#!/usr/bin/env python
# coding: utf-8

# # Workspace for Project Euler problems
# 
# ## Problem 7
# 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?

# In[1]:


import primetools as pt


# In[2]:


pt.findSomePrimes(20)


# In[3]:


pt.findSomePrimes(number=20)


# In[7]:


sp=pt.findSomePrimes(number=10001)


# In[23]:

spkeys=list(sp.keys())
spkeys.reverse()
print (spkeys[0])

