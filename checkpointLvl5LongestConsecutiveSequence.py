'''
You can find 3 Diffrent type solutions for this challange

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Example:
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.


'''

# PYTHON 3
#<------------------------type 1---------------->#
import random

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        # Create a set with all the values in it
        vals = set()
        for elem in A:
            vals.add(elem)
            
        # Pick a value and keep searching on both sides of array
        # Repeat process until all elements in set are removed
        maxLen = 1
        while len(vals) > 0:
            val = random.sample(vals, 1)[0] # we know the length is greater than 0
            left = val-1
            right = val+1
            curLen = 1
            vals.remove(val) # remove this element since already visited
  
            while left in vals:
                curLen += 1
                vals.remove(left) # remove from the set to avoid visiting again
                left -=1 
            while right in vals:
                curLen += 1
                vals.remove(right)
                right += 1
            maxLen = max(curLen, maxLen)
        return maxLen
        
#<------------------------type 2---------------->#        
 class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        if len(A) <= 1:
            return len(A)
            
        max_len = 0
        mySet = set(A)
        
        for x in A:
            if x - 1 not in mySet:
                c = 1
                x += 1
                while x in mySet:
                    c += 1
                    x += 1
                    
                max_len = max(c, max_len)
                
        return max_len


#<------------------------type 3---------------->#
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        dct = {}
        for elem in A:
            if elem not in dct:
                if elem-1 in dct:
                    dct[elem] = dct[elem-1] + 1
                else:
                    dct[elem] = 1
                update = True
                tmp = elem+1
                while update:
                    if tmp in dct:
                        dct[tmp] = dct[tmp-1] + 1
                        tmp+= 1
                    else:
                        update = False
        return max(dct.values())
            


