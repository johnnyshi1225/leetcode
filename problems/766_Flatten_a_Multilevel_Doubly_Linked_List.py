#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-18 23:03:15
# File Name: 766_Flatten_a_Multilevel_Doubly_Linked_List.py
# Description:
#########################################################################


# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        h, t = self.__flatten(head)
        return h

    def __flatten(self, head):
        if not head:
            return None, None
        h = t = None
        while head:
            n = Node(head.val, t, None, None)
            if t:
                t.next = n
                t = n
            else:
                h = t = n
            if head.child:
                ch, ct = self.__flatten(head.child)
                ch.prev = t
                t.next = ch
                t = ct
            head = head.next
        return h, t


h = t = Node(1, None, None, None)
n = Node(2, h, None, Node(3, None, None, None))
t.next = n
t = n
n = Node(4, t, None, None)
t.next = n
t = n

h = Solution().flatten(h)
while h:
    print(h.val)
    h = h.next
# vim: set expandtab ts=4 sts=4 sw=4 :
