#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-11 14:06:22
# File Name: simple_linked_list.py
# Description:
#########################################################################


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def linked_list(l):
    head = None
    cur = None
    for i in l:
        n = ListNode(i)
        if not head:
            head = n
        else:
            cur.next = n
        cur = n
    return head


def print_linked_list(head):
    ret = head
    while ret:
        print(ret.val)
        ret = ret.next


if __name__ == "__main__":
    ret = linked_list(range(10))
    print_linked_list(ret)
# vim: set expandtab ts=4 sts=4 sw=4 :
