
from functools import reduce
import numbers

def highestConsecutiveProduct(numlist, conseclength = 4):
    
    """Find the highest product of consecutive digits in a list.
    
    RETURNS:
        pos 0: the product
        pos 1: the beginning index of the number sequence
        pos 2: the subsequence itself"""
    
    if isinstance(numlist, numbers.Number):
        numlist=str(numlist)
    nl=[int(x) for x in numlist]
    
    if len(nl) < conseclength:
        raise Exception("the length of the sequences cannot be less \
        than the requested subsequence length")
        
    getsubseq=lambda idx: nl[idx-conseclength+1:idx+1]
    getprod=lambda idx: reduce((lambda x,y: x*y), getsubseq(idx))
    mx=0
    mxidx=-1
    largestss=[]
    # how many digits read since last 0 was encountered
    lastzero=0
    for i in range(0, len(nl)):
        nex=nl[i]
        if nex == 0:
            lastzero=0
        else:
            lastzero+=1
        if lastzero >= conseclength:
            prod=getprod(i)
            if prod > mx:
                mx=prod
                mxidx=i-conseclength+1
                largestss=getsubseq(i)
        
    return [mx, mxidx, largestss]