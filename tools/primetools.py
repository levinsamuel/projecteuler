#!/usr/bin/env python
# coding: utf-8

# # tools around finding prime numbers and factoring
# 

import math, logging, sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required. Found version is: "
    + sys.version)

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

log = logging.getLogger("primetools")
log.setLevel(logging.INFO)


def findSomePrimes(limit = 0, number = 0):

    '''Method that returns a map where each key is a prime number. The value of the map will be 
initialized to 0. This is for counting prime factors of some other number.'''
    
    def _addIfPrime(i, someprimes):
        prime=True
        sqroot=math.sqrt(i);
        for p in someprimes:
            if i % p == 0:
                prime=False
                break
            elif p > sqroot:
                break
        if prime:
            someprimes[i]=0
    
    limit=int(limit)
    someprimes={2:0}
    if limit > 0:
        for i in range(3, limit+1, 2):
            if i % 10000 == 1:
                log.debug("On number: %d", i-1)
            _addIfPrime(i, someprimes)
    elif number > 0:
        i=3
        while len(someprimes) < number:
            _addIfPrime(i, someprimes)
            i += 2
    else:
        raise Exception("Either limit or number parameter must be specified and greater than 0.")

    return someprimes


def factor(num, primes=None):
    
    """Return the prime factorization of a number in the form of a map between 
the prime key and the number of those primes in the prime factorization

This runs much faster if a list of primes is provided."""

    root=math.ceil(math.sqrt(num)) + 1
    factors={}
    numagain=num
    looper=primes if primes is not None else range(2, root)
    for i in looper:
        if i > root:
            break
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


def getDivisors(num):
    
    """Return the divisors of a given number. This is quite slow."""
    mx=math.ceil(num/2) + 1
    factors=[1,num]
    numagain=num
    for i in range(2, mx):
        n=numagain/i
        if n.is_integer():
            factors.append(i)
    
    return factors;

def smallestCommonMultiple(num):
    """Find the smallest number that is divisible by every number from one to 
num. It does this by finding all the prime factorizations of each number 
and making sure the final map has exactly as many of each prime factor as 
the greatest number of any number up to num."""
    
    primes = findSomePrimes(num)
    log.debug("primes: {}".format(primes))
    
    for i in range(2, num+1):
        fs=factor(i)
        log.debug("factors of {}: {}".format(i, fs))
        for pm in fs:
            primes[pm] = max(primes[pm], fs[pm])
    
    return primes


if __name__ == '__main__':

    primef=smallestCommonMultiple(20)
    num=1
    for k in primef:
        num *= (k**primef[k])
        
    print ("smallest number divisible by 1-20: {}".format(num))

