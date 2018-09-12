#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-10 19:20:01
# File Name: 206_Reverse_Linked_List.py
# Description:
#########################################################################
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # not in-place
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        new_head = None
        while cur:
            if not new_head:
                new_head = ListNode(cur.val)
            else:
                node = ListNode(cur.val)
                node.next = new_head
                new_head = node
            cur = cur.next
        return new_head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
ret = Solution().reverse(head)
while ret:
    print(ret.val)
    ret = ret.next
# vim: set expandtab ts=4 sts=4 sw=4 :
