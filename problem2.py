#!/usr/bin/env python
# coding: utf-8

# # Workspace for Project Euler problems
# 
# ## Problem 2
# 
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# ### Approach
# 
# #### Observation 1
# 
# Firstly, every third Fibonacci number will be even. If the first two are 1 and 2, (odd, even), the next will be odd because odd+even=odd. Then the prior two are (even, odd), so the next one will be odd for the same reason. Then the prior two are odd, so the next will be even because odd+odd=even. Then the prior two are (odd, even), and we can see that the pattern has repeated.

# #### Observation 2
# 
# Here are the progressive sums of the Fibonacci numbers:
# 
# $$1, 3, 6, 11, 19, 32, 53, 87, ...$$
# 
# This sequence is in its own respect a Fibonacci-like sequence where instead of the rule being:
# 
# $$x_{n} + x_{n+1} = x_{n+2}$$
# 
# it is:
# 
# $$x_{n} + x_{n+1} + 2 = x_{n+2}$$

# #### Observation 3
# 
# Each Fibonacci number is the sum of the prior two. Since every third number is even, these two facts combined mean that adding up the entire sequence is just double the sum of the even numbers, plus or minus some trailing leftovers. In other words, taking this subset of the sequence:
# 
# $$3, 5, 8, 13, 21, 34$$
# 
# To find the sum of the even portion of this subsequence, you can add the even numbers, but also 8 is just 3+5, and 34 is just 13+21, so the half the total sum is just the sum of the even numbers.

# #### Observation 4
# 
# Let's start the Fibonacci sequence above with two 1's, as it is sometimes done. So $[1, 1, 2, 3, 5, 8, 13, 21, ...]$. And for ease let's call that sequence $F$. The progressive sums then look like this:
# 
# $$1, 2, 4, 7, 12, 20, 33, 54$$
# 
# This is again similar to the other progressive sum sequence but with the rule which I will call $F_2$:
# 
# $$F_2 := x_{n} + x_{n+1} + 1 = x_{n+2}$$
# 
# But this sequence has the advantage that, since it starts with two odds, it more accurately follows the pattern described in [Observation 3](#Observation-3). Therefore, at the occurence of each even number, this sequence represents double the sum of the even numbers up to that point (e.g. the sixth number in regular Fibonacci is 8, and the sixth in the above is 20, double the sum of the two even numbers to occur in regular Fibonacci to that point).

# #### Observation 5
# 
# We only really care about every third value of $F_2$, since it's only those that represent progressive 

# #### Claim
# 
# Therefore, another way to solve this problem is to find out how many Fibonacci numbers are below 4M, go to that same point in the sequence $F_2$, round down to the nearest sequence index multiple of three (since only every three Fibonacci are even), and take half that value. The problem is that this doesn't seem any more computationally efficient than just brute-forcing it.
# 
# #### Observation 6
# 
# However, as we're calculating $F_2$, then say we obtain term $x_i$ in the sequence. Since the sequence is the cumulative sum of the Fibonacci sequence, then the differece between $x_i$ and $x_{i-1}$ is the value of $y_i$, where $y_i$ is the $i$th term in $F$. This means that as soon as the difference between $x_i$ and $x_{i-1}$ exceeds 4M, we stop.
# 
# #### Observation 7
# 
# But we also know that in $F_2$:
# 
# $$x_{n} + x_{n+1} + 1 = x_{n+2}$$
# 
# Therefore:
# 
# $$x_{n+2} - x_{n+1} = x_{n} + 1$$
# 
# Therefore, if $x_n$ is greater than or equal to 4M, that means the sequence value in $F$ for index $n+2$ is greater than 4M and the sum should terminate.

# In[18]:


import logging, sys;

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
log = logging.getLogger("main")
log.setLevel(logging.INFO)

x0=1
x1=2
x2=0
while (1):
    if (x0 >= 4000000):
        break;
    x2 = x0 + x1 + 1;
    x0 = x1;
    x1 = x2;
    
evensum = x2//2;

print ('Sum of even numbers: {0}'.format(evensum))
