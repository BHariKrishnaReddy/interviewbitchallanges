'''
Given a singly linked list, modify the value of first half nodes such that :

    1.1st node’s new value = the last node’s value - first node’s current value
    2.2nd node’s new value = the second last node’s value - 2nd node’s current value,

and so on …

    NOTE :

        If the length L of linked list is odd, then the first half implies at first floor(L/2) nodes. So, if L = 5, the first half refers to first 2 nodes.
        If the length L of linked list is even, then the first half implies at first L/2 nodes. So, if L = 4, the first half refers to first 2 nodes.

Example :

Given linked list 1 -> 2 -> 3 -> 4 -> 5,

You should return 4 -> 2 -> 3 -> 4 -> 5
as

for first node, 5 - 1 = 4
for second node, 4 - 2 = 2
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        l = 0
        last = A
        table = dict()
    
        while last is not  None :
            table[l] = last
            l = l + 1
            last = last.next
           
        half = l // 2
    
        last = l - 1
    
        for i in range(0,half) :        
            n1 = table[i]
            n2 = table[last]
            n1.val = n2.val - n1.val        
            last = last - 1
            
        return A
