#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-19 22:14:37
# File Name: Copy_List_with_Random_Pointer.py
# Description:
#########################################################################
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        tmp = RandomListNode(0)
        tail = tmp
        cur = head
        while cur:
            n = RandomListNode(cur.label)
            if cur.random:
                n.random = RandomListNode(cur.random.label)
            tail.next = n
            cur = cur.next
            tail = tail.next
        return tmp.next
# vim: set expandtab ts=4 sts=4 sw=4 :
