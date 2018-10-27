
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