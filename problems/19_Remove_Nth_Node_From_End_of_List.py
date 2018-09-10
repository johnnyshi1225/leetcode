#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-10 14:52:28
# File Name: 19_Remove_Nth_Node_From_End_of_List.py
# Description:
#########################################################################
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        i = 1
        cur = head
        target = None
        prev = None
        while cur:
            if target:
                prev = target
                target = target.next
            if i == n:
                target = head
            cur = cur.next
            i += 1
        if target == head:
            head = target.next
            target.next = None
        else:
            prev.next = target.next
            target.next = None
        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
ret = Solution().removeNthFromEnd(head, 1)
while ret:
    print(ret.val)
    ret = ret.next
# vim: set expandtab ts=4 sts=4 sw=4 :
