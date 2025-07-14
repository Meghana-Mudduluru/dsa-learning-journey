'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.



Example 1:

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:

Input: head = [0]
Output: 0

Constraints:

    The Linked List is not empty.
    Number of nodes will not exceed 30.
    Each node's value is either 0 or 1.

'''

from typing import List

# Definition for singly-linked list.
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0
        while head:
            num = (num << 1) | head.val
            head = head.next
        return num

# Convert a list like [1, 0, 1] to a linked list
def build_linked_list(lst):
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

h = [1,0,1]
head = build_linked_list(h)

sol=Solution()
print(sol.getDecimalValue(head))