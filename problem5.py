#!/usr/bin/env python
# coding: utf-8

# # Workspace for Project Euler problems
# 
# ## Problem 5
# 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# In[46]:


import math, logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.INFO)

log = logging.getLogger("main")
log.setLevel(logging.INFO)


# In[17]:


def findSomePrimes(limit):
    "Method that returns a map where each key is a prime number. The     value of the map will be initialized to 0. This is for counting     prime factors of some other number."
    someprimes={2:0}
    for i in range(3, limit+1):
        prime=True
        for p in someprimes:
            if i % p == 0:
                prime=False
                break
        if prime:
            someprimes[i]=0
    return someprimes

findSomePrimes(100)


# In[40]:


def factor(num):
    
    "Return the prime factorization of a number in the form of a map     between the prime key and the number of those primes in the prime     factorization"
    root=math.ceil(math.sqrt(num))
    factors={}
    numagain=num
    for i in range(2, root+1):
        n=numagain/i
        instances=0
        while n.is_integer():
            numagain=n
            instances += 1
            n=numagain/i
        if instances > 0:
            factors[i]=instances
    
    if numagain > 1:
        factors[int(numagain)]=1
    return factors;

log.debug("factor 69: {}".format(factor(69)))
log.debug("factor 4: {}".format(factor(4)))


# In[44]:


def smallestCommonMultiple(num):
    "Find the smallest number that is divisible by every number from     one to num. It does this by finding all the prime factorizations     of each number and making sure the final map has exactly as many     of each prime factor as the greatest number of any number up to num."
    primes = findSomePrimes(num)
    log.debug("primes: {}".format(primes))
    
    for i in range(2, num+1):
        fs=factor(i)
        log.debug("factors of {}: {}".format(i, fs))
        for pm in fs:
            primes[pm] = max(primes[pm], fs[pm])
    
    return primes
    
smallestCommonMultiple(10)


# In[45]:


primef=smallestCommonMultiple(20)
num=1
for k in primef:
    num *= (k**primef[k])
    
print ("smallest number divisible by 1-20: {}".format(num))

