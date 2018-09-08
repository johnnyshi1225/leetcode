#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-08 13:46:42
# File Name: Linked_List_Cycle_II.py
# Description:
#########################################################################
"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        slow_ptr = head
        fast_ptr = head

        while True:
            slow_ptr = self.__forward(slow_ptr, 1)
            fast_ptr = self.__forward(fast_ptr, 2)
            if fast_ptr is None:
                return None
            elif slow_ptr == fast_ptr:
                slow_ptr = head
                break
        while slow_ptr != fast_ptr:
            slow_ptr = self.__forward(slow_ptr, 1)
            fast_ptr = self.__forward(fast_ptr, 1)
        return slow_ptr

    def __forward(self, cur, step):
        for i in range(step):
            if cur:
                cur = cur.next
            else:
                return None
        return cur


head = ListNode(1)
head.next = ListNode(2)
head.next.next = head
ret = Solution().detectCycle(head)
print(ret.val)
# vim: set expandtab ts=4 sts=4 sw=4 :
