#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-12 13:35:44
# File Name: 234_Palindrome_Linked_List.py
# Description:
#########################################################################
from simple_linked_list import linked_list, print_linked_list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        i = 0
        l = []
        cur = head
        while cur:
            l.append(cur.val)
            cur = cur.next
            i += 1
        cur = head
        while l:
            if cur.val == l.pop():
                cur = cur.next
            else:
                return False
        return True



head = linked_list([1, 2, 2, 1])
head = linked_list([1, 2, 3, 4])
ret = Solution().isPalindrome(head)
print(ret)
# vim: set expandtab ts=4 sts=4 sw=4 :
