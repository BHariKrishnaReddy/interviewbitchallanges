/*
Print concentric rectangular pattern in a 2d matrix.
Let us show you some examples to clarify what we mean.
Example 1:
Input: A = 4.
Output:

4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 

Example 2:

Input: A = 3.
Output:

3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3 

The outermost rectangle is formed by A, then the next outermost is formed by A-1 and so on.
You will be given A as an argument to the function you need to implement, and you need to return a 2D array.
*/


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        length = 2 * A - 1
        lli = [[0 for x in range(length)] for y in range(length)]
        for i in range(length):
            for j in range(length):
                if(abs(i - (A - 1)) > abs(j - (A - 1))):
                    lli[i][j] = abs(i - (A - 1)) + 1
                else:
                    lli[i][j] = abs(j - (A - 1)) + 1
        return lli
