#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-09 22:11:42
# File Name: Intersection_of_Two_Linked_Lists.py
# Description:
#########################################################################

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        cur_a = headA
        cur_b = headB
        len_a = 0
        len_b = 0
        while cur_a or cur_b:
            if cur_a:
                cur_a = cur_a.next
                len_a += 1
            if cur_b:
                cur_b = cur_b.next
                len_b += 1
        long_head = headA
        short_head = headB
        if len_a < len_b:
            long_head = headB
            short_head = headA
        for i in range(abs(len_a - len_b)):
            long_head = long_head.next
        while long_head:
            if short_head == long_head:
                return short_head
            else:
                short_head = short_head.next
                long_head = long_head.next
        return None


headA = ListNode('a1')
headA.next = ListNode('a2')
headA.next.next = ListNode('a3')

headB = ListNode('b1')
# vim: set expandtab ts=4 sts=4 sw=4 :
