class Solution:
    def numfun1(self, A, B):
        i,j,sequences,sum_sequence = 0,0,0,A[0]
        while i<len(A):
            if sum_sequence>=B:
                if i<=j:
                    sequences += (len(A)-j)
                    sum_sequence -= A[i]
                    i += 1
            elif j<len(A)-1 :
                j += 1
                sum_sequence += A[j]
            else:
                break
        return sequences
# @param A : list of integers
# @param B : integer
# @param C : integer
# @return an integer
    def numRange(self, A, B, C):
        return self.numfun1(A, B)-self.numfun1(A, C+1)
