#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-19 21:48:11
# File Name: 61_Rotate_List.py
# Description:
#########################################################################
from simple_linked_list import linked_list, print_linked_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        length = 0
        prev = None
        cur = head
        while cur:
            prev = cur
            cur = cur.next
            length += 1
        tail = prev
        k = k % length
        if k == 0 or length == 1:
            return head

        cur = head
        for _ in range(length - k - 1):
            cur = cur.next
        tail.next = head
        head = cur.next
        cur.next = None
        return head


head = linked_list([1, 2, 3, 4, 5])
ret = Solution().rotateRight(head, 2)
print_linked_list(ret)
# vim: set expandtab ts=4 sts=4 sw=4 :
