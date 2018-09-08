#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-08 13:35:27
# File Name: Linked_List_Cycle.py
# Description:
#########################################################################


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        slow_ptr = head
        fast_ptr = head

        while True:
            slow_ptr = self.__forward(slow_ptr, 1)
            fast_ptr = self.__forward(fast_ptr, 2)
            if fast_ptr is None:
                return False
            elif slow_ptr == fast_ptr:
                return True

    def __forward(self, cur, step):
        for i in range(step):
            if cur:
                cur = cur.next
            else:
                return None
        return cur

# vim: set expandtab ts=4 sts=4 sw=4 :
