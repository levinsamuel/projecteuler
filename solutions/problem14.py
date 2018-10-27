#!/usr/bin/env python
# coding: utf-8

# # Workspace for Project Euler problems
# 
# ## Problem 14
# 
# The following iterative sequence is defined for the set of positive integers:
# 
# $$n \to \frac{n}{2} \text{ ($n$ is even)}$$
# $$n \to 3n + 1 \text{ ($n$ is odd)}$$
# 
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# $$13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1$$
# 
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.

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


# ## Approach
# 
# It is clear that, starting at any given number, the sequence is deterministic, meaning the length of the sequence after that number will always be the same length (e.g. 10 long for the number 13). Therefore, for a new number of unknown length, then as soon as a term with known length occurs, we know the length of the full sequence. Additionally, we know the legnth of the sequence for all the unknown terms that occur after it as well (e.g. we know from the above sequence that the length of the sequence for 40 is 9, for 20 is 8, etc.). So hopefully calculating the sequence length for each number is relatively linear to the number of numbers

# In[19]:


a=[1,2,4]
y={x:x**2 for x in a}
print (y)
print (y[2])
y.update({x+5:x+7 for x in a})
print (y)


# In[46]:


def find_sequence_lengths(upto):
    '''Find all the lengths of all the sequences starting with each number
from 1 to "upto" parameter. Returns a map from the number to the length of its
sequence'''
    lengths={1:1}
    for start in range(1, upto):
        li, i = [], start
        while True:
            try:
                # If no key error thrown, map contains i, break loop
                lengths[i]
                break
            except KeyError:
                # map does not contain key, add to list and find next i
                li.append(i)
                i = int(i/2) if i % 2 == 0 else 3*i + 1
        # If there are items in the list, i.e. items not known, add
        # them to the map, increasing from the first found existing length
        if len(li) > 0:
            li.reverse()
            lengths.update({li[x]:x+1+lengths[i] for x in range(len(li))})
        
    return lengths


# In[44]:


lengths=find_sequence_lengths(1000000)


# In[50]:


mx, nm = 0, 0
for num, lngt in lengths.items():
    if lngt > mx and num < 1000000:
        mx, nm = lngt, num
        
print("The longest sequence starts at {}, and is {} long.".format(nm, mx))

n=837799
for i in range(1, 1000000):
    n = n//2 if n % 2 == 0 else 3*n+1
    if n == 1:
        break
print(i)


# In[ ]:




