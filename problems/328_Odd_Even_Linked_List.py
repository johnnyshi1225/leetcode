#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-11 13:46:04
# File Name: 328_Odd_Even_Linked_List.py
# Description:
#########################################################################
from simple_linked_list import linked_list, print_linked_list
"""
Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # not in-place
        if not head:
            return None
        odd_head = None
        odd_tail = None
        even_head = None
        even_tail = None
        i = 1
        cur = head
        while cur:
            n = ListNode(cur.val)
            if i % 2 != 0:
                if odd_tail:
                    odd_tail.next = n
                    odd_tail = n
                else:
                    odd_head = n
                    odd_tail = n
            else:
                if even_tail:
                    even_tail.next = n
                    even_tail = n
                else:
                    even_head = n
                    even_tail = n
            cur = cur.next
            i += 1
        head = odd_head
        odd_tail.next = even_head
        return head


head = linked_list([2, 1, 3, 5, 6, 4, 7])
head = linked_list([1, 2, 3])
ret = Solution().oddEvenList1(head)
print_linked_list(ret)
# vim: set expandtab ts=4 sts=4 sw=4 :
