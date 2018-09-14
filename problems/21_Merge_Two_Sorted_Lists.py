#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-14 13:17:08
# File Name: 21_Merge_Two_Sorted_Lists.py
# Description:
#########################################################################
from simple_linked_list import ListNode, linked_list, print_linked_list


class Solution:
    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        tail = None
        if not l1 and not l2:
            return None
        if l1 and not l2:
            head = l1
            return head
        elif l2 and not l1:
            head = l2
            return head

        while l1 and l2:
            if l1.val <= l2.val:
                if not head:
                    head = l1
                    tail = l1
                else:
                    tail.next = l1
                    tail = l1
                l1 = l1.next
            else:
                if not head:
                    head = l2
                    tail = l2
                else:
                    tail.next = l2
                    tail = l2
                l2 = l2.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        return head

    # 简洁版本
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = tail = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        return head.next


head1 = linked_list([1, 2])
head2 = linked_list([1, 2, 3, 4])
ret = Solution().mergeTwoLists(head1, head2)
print_linked_list(ret)
# vim: set expandtab ts=4 sts=4 sw=4 :
