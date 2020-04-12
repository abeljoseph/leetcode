# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            if l1:
                return l1
            elif l2:
                return l2
            return

        head = ListNode(None)
        if l1.val > l2.val:
            head.val = l2.val; l2 = l2.next
        else:
            head.val = l1.val; l1 = l1.next

        curr_node = head
        while l1 or l2:
            if not l1 or not l2:  # One of the lists are at the end
                if not l1:
                    curr_node.next = l2; l2 = l2.next
                elif not l2:
                    curr_node.next = l1; l1 = l1.next
                curr_node = curr_node.next
                continue

            if l2.val > l1.val:
                curr_node.next = l1; curr_node = curr_node.next; l1 = l1.next
            else:
                curr_node.next = l2; curr_node = curr_node.next; l2 = l2.next

        return head
