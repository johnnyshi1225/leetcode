#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-20 13:31:33
# File Name: 816_Design_HashSet.py
# Description:
#########################################################################
"""
All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__bucket_size = 10000
        self.__buckets = [None] * self.__bucket_size

    def __hash(self, key):
        index = key % self.__bucket_size
        return index

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key is None:
            return
        index = self.__hash(key)
        bucket = self.__buckets[index]
        if bucket:
            cur = bucket
            tail = None
            while cur:
                if cur.val == key:
                    return
                else:
                    tail = cur
                    cur = cur.next
            n = Node(key)
            tail.next = n
            tail = n
        else:
            self.__buckets[index] = Node(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key is None:
            return
        index = self.__hash(key)
        bucket = self.__buckets[index]
        if bucket:
            prev = None
            cur = bucket
            while cur:
                if cur.val == key:
                    if prev:
                        prev.next = cur.next
                    else:
                        self.__buckets[index] = cur.next
                    del cur
                    return
                prev = cur
                cur = cur.next
        else:
            return

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key is None:
            return False
        index = self.__hash(key)
        bucket = self.__buckets[index]
        if bucket:
            cur = bucket
            while cur:
                if cur.val == key:
                    return True
                cur = cur.next
            return False
        else:
            return False


hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)
print(hashSet.contains(1))
print(hashSet.contains(3))
hashSet.add(2)
print(hashSet.contains(2))
hashSet.remove(2)
print(hashSet.contains(2))
# vim: set expandtab ts=4 sts=4 sw=4 :
