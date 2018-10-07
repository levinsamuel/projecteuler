#!/usr/bin/env python
# coding: utf-8

# # Workspace for Project Euler problems
# 
# ## Problem 4
# 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

# In[1]:


999*999


# In[32]:


import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.INFO)
log = logging.getLogger("main")
log.setLevel(logging.WARNING)


# In[15]:


def isPalindrome(num):
    "Check if input parameter is a palindrome."
    log.debug("Num: {0}".format(num))
    digits=[]
    while num > 0:
        digits.append(num%10)
        num=num//10
    log.debug("digits: {0}".format(digits))
    while len(digits) > 1:
        st=digits.pop()
        en=digits.pop(0)
        if st != en:
            return False
    return True


# In[18]:


isPalindrome(15)


# In[20]:


isPalindrome(151)


# In[26]:


list(range(5,1, -1))


# ### Observation 1
# 
# The largest such number will likely begin with a 9, which means it will end with a 9. Also the product of the two largest 3-digit numbers above is 998001, six digits, so the final number will probably be six digits. If we assume that the largest palindrome will start with a 9, then we only have to check three-digit number pairs that end with the digits [1,9], [3,3] or [7,7], since any other combination will produce a product with a last digit other than 9. Then, if it turns out there are no such palindromes beginning with 9, we can do the same with 8, which is the pairs [2,4], [8.1], [8,6], [3,6], [4,7], [2,9]. Etc. However that may be complicated to implement and may ultiple save no time.

# In[42]:


def checkPalindromes(maxN):
    highestP=0
    factors=[]
    for num1 in range(maxN, 0, -1):
        if num1**2 < highestP:
            log.info("the next number {} is less than the root of the highest palindrome {}, returning".format(
                     num1, highestP))
            break
        for num2 in range(num1, 0, -1):
            prod=num1*num2
            if highestP >= prod:
                break
            elif isPalindrome(prod):
                highestP=prod
                factors=[num1, num2]
                break
    factors.append(highestP)
    return factors


# In[43]:

answer=checkPalindromes(999)
print ("The highest palindrome is {}, with factors {} and {}.".format(answer[2], answer[0], answer[1]))

