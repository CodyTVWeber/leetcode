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
        while cur_node.next is not None:
            cur_node = cur_node.next
            num1 = str(cur_node.val) + num1

        cur_node = l2
        while cur_node.next is not None:
            cur_node = cur_node.next
            num2 = str(cur_node.val) + num2

        num3 = int(num1) + int(num2)
        num3_string = str(num3)
        split_num3 = list(num3_string)
        nodes = [ListNode(int(x)) for x in reversed(split_num3)]
        nodes_length = len(nodes)
        for nodeIndex in range(nodes_length):
            cur_node = nodes[nodeIndex]
            if nodeIndex + 1 < nodes_length:
                cur_node.next = nodes[nodeIndex + 1]

        return nodes[0]
