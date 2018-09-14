#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-10 19:20:01
# File Name: 206_Reverse_Linked_List.py
# Description:
#########################################################################
from simple_linked_list import linked_list, print_linked_list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # not in-place
    def reverseList1(self, head):
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

    # in-place
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        while head:
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
        return new_head


head = linked_list([1, 2, 3, 4])
ret = Solution().reverseList(head)
print_linked_list(ret)
# vim: set expandtab ts=4 sts=4 sw=4 :
