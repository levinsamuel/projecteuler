#!/usr/bin/env python
# coding: utf-8

# # Workspace for Project Euler problems
# 
# ## Problem 9
# 
# A Pythagorean triplet is a set of three natural numbers, $a < b < c$, for which,
# 
# $$a^2 + b^2 = c^2$$
# 
# For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.
# 
# There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.
# Find the product $abc$.

# In[54]:


import tools.primetools as pt
import numbers, math
import tools.misc as misc
import logging, sys
from functools import reduce

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

log = logging.getLogger("main")

# DEBUG, INFO, WARNING, ERROR, CRITICAL
log.setLevel(logging.DEBUG)


# ### Some random substitution just looking for stuff
# 
# 1.1: $a + b + c = 1000$
# 
# 1.2: $c = 1000 - a - b$
# 
# 2: $a^2 + b^2 = c^2$
# 
# 3, 1.1 squared:
# $a^2 + 2ab + b^2 + 2bc + c^2 + 2ac = 1000000$
# 
# 4, Substitute 2: $2a^2 + 2ab + 2b^2 + c(2b + 2a) = 1000000$
# 
# 5, Substitute 1.2: $2a^2 + 2ab + 2b^2 + (1000 - a - b)(2b + 2a) = 1000000$
# 
# 6: $(1000 - a - b)(2b + 2a) = 2000b + 2000a - 4ab - 2a^2 - 2b^2$
# 
# 7: $-4ab - 2a^2 - 2b^2 = -2(2ab + a^2 + b^2) = -2(a + b)^2$
# 
# 8, Substitute 6: $-2ab + 2000a + 2000b = 1000000$
# 
# 9: $a^2 + b^2 = (a + b)^2 - 2ab$
# 
# 10: $c^2 = (1000 - c)^2 - 2ab$
# 
# 11: $(1000 - c)^2 = 1000000 - 2000c + c^2$
# 
# 12: $2000c + 2ab = 1000000$

# ### Ok what did we learn
# 
# From [8], we know that $-2ab$ must be a multiple of 1000, since the other terms in the equation are, so $ab$ must be a multiple of 500 between them.

# ### Not sure about this
# 
# Instead I'll just start with the fact that
# 
# $$(2x, x^2-1, x^2+1)$$
# 
# for any $x$ is a pythagorean triplet, and just search those for sets that sum to 1000. We'll see if that works first.
# 
# The sum of those three is, easily enough:
# 
# $$2x + 2x^2$$

# In[66]:


# Another way would be to find the one that is a factor of 1000
# random value that will satisfy loop
summ=3
x=1
while summ < 1000 and 1000 % summ is not 0:
    x+=1
    summ = 2*x + 2*(x**2)
    
print (f"Sum: {summ}, x:{x}")
if summ <= 1000:
    print ("found it")
    multiplier=1000/summ
    ret = {'a':2*x*multiplier, 'b':multiplier*(x**2-1),
          'c':multiplier*(x**2+1)}
    print (f"Solution: {ret}")


# So I guess it didn't.

# ### I'll try to put $a$ in terms of $c$ and then while trying different values of $c$ we can then solve for $a$ and $b$
# 
# $$b = 1000 - c - a$$
# 
# $$a^2 + (1000 - a - c)^2 = c^2$$
# 
# $$a^2 + 1000000 - 2000a - 2000c + 2ac + a^2 + c^2 = c^2$$
# 
# $$2a^2 + 1000000 - 2000a - 2000c + 2ac = 0$$
# 
# $$2a^2 + 1000000 - 2000a - c(2000 - 2a) = 0$$
# 
# $$c = \frac{a^2 - 1000a + 500000}{1000 - a}$$

# In[48]:


cfroma = lambda a: ((a**2) - (1000*a) + 500000)/(1000 - a)
cfroma(200)


# In[53]:


log.setLevel(logging.INFO)
pc = {}
for a in range(333, 1, -1):
    # possible values of c 
    c = cfroma(a)
    log.debug("trying a: %d. c is %f", a, c)
    if c.is_integer():
        pc[a] = c
        
print (pc)

if len(pc) is not 1:
    raise Exception("There should be only one pythagorean triple")

for a,c in pc.items():
    b = 1000 - a - c
    ret = {'a':a, 'b':b, 'c':c}
    print(f"b: {b}, a sq plus b sq: {a**2 + b**2}, c sq: {c**2}")

print (ret)


# In[57]:


prod= reduce(lambda x,y:x*y, ret.values())

print (f"Product is: {prod}")

