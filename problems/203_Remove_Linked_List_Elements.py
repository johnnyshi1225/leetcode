#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-11 13:18:01
# File Name: 203_Remove_Linked_List_Elements.py
# Description:
#########################################################################
# Remove all elements from a linked list of integers that have value val.
#
# Example:
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev = None
        cur = head
        while cur:
            if val == cur.val:
                if prev:
                    prev.next = cur.next
                    cur.next = None
                    cur = prev.next
                else:
                    head = head.next
                    del cur.next
                    cur = head
            else:
                prev = cur
                cur = cur.next
        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
ret = Solution().removeElements(head, 1)
while ret:
    print(ret.val)
    ret = ret.next
# vim: set expandtab ts=4 sts=4 sw=4 :
