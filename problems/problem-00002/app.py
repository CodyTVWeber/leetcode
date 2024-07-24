from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = str(l1.val)
        num2 = str(l2.val)

        cur_node = l1
        while cur_node.next:
            num1 = num1 + str(cur_node.val)
            cur_node = cur_node.next

        cur_node = l2
        while cur_node.next:
            num2 = num2 + str(cur_node.val)
            cur_node.val = cur_node.next

        num3 = int(num1) + int(num2)
        num3_string = str(num3)
        split_num3 = num3_string.split('')
        nodes = [ListNode(int(x)) for x in reversed(split_num3)]
        nodes_length = len(nodes)
        for nodeIndex in range(nodes_length):
            cur_node = nodes[nodeIndex]
            if nodeIndex < nodes_length:
                cur_node.val = nodes[nodeIndex + 1]

        return nodes[0]
