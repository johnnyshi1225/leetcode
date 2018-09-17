#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-17 23:37:52
# File Name: 2_Add_Two_Numbers.py
# Description:
#########################################################################
from simple_linked_list import ListNode, linked_list, print_linked_list


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        tail = head
        add = 0
        while l1 or l2:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            s = val1 + val2 + add
            if s >= 10:
                add = 1
                s = s % 10
            else:
                add = 0
            n = ListNode(s)
            tail.next = n
            tail = n
        if add == 1:
            n = ListNode(1)
            tail.next = n
            tail = n
        return head.next


head1 = linked_list([1, 2])
head2 = linked_list([1, 2, 3, 4])
head1 = linked_list([5])
head2 = linked_list([5])
ret = Solution().addTwoNumbers(head1, head2)
print_linked_list(ret)
# vim: set expandtab ts=4 sts=4 sw=4 :
