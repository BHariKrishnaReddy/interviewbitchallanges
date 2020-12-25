'''
Given an array, find the next greater element G[i] for every element A[i] in the array. The Next greater Element for an element A[i] is the first greater element on the right side of A[i] in array.
More formally,

G[i] for an element A[i] = an element A[j] such that 
    j is minimum possible AND 
    j > i AND
    A[j] > A[i]

Elements for which no greater element exist, consider next greater element as -1.

Example:

Input : A : [4, 5, 2, 10]
Output : [5, 10, 10, -1]

Example 2:

Input : A : [3, 2, 1]
Output : [-1, -1, -1]
'''


def getGth(A, st):
  while len(st) > 0:
      if st[-1] > A:
        return st[-1]
        
      st.pop()
  return -1

class Solution:
# @param A : list of integers
# @return a list of integers
    def nextGreater(self, A):
        st = []
        gts = []
        for i in range(len(A)-1,-1,-1):
            gts.append(getGth(A[i],st))
            st.append(A[i])
        
        return gts[::-1]
