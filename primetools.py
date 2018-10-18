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


def findSomePrimes(limit):
    "Method that returns a map where each key is a prime number. The value of the map will be \
	initialized to 0. This is for counting prime factors of some other number."
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


def factor(num):
    
    "Return the prime factorization of a number in the form of a map between the prime key and \
	the number of those primes in the prime factorization"
    root=math.ceil(math.sqrt(num)) + 1
    factors={}
    numagain=num
    for i in range(2, root):
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


def smallestCommonMultiple(num):
    "Find the smallest number that is divisible by every number from one to num. It does this by \
	finding all the prime factorizations     of each number and making sure the final map has \
	exactly as many of each prime factor as the greatest number of any number up to num."
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

