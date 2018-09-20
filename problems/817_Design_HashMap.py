#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-20 23:17:35
# File Name: 817_Design_HashMap.py
# Description:
#########################################################################


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Pair:
    def __init__(self, k, v):
        self.key = k
        self.value = v


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__bucket_size = 10000
        self.__buckets = [None] * self.__bucket_size

    def __hash(self, key):
        index = key % self.__bucket_size
        return index

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        if key is None:
            return
        p = Pair(key, value)
        index = self.__hash(key)
        bucket = self.__buckets[index]
        if bucket:
            cur = bucket
            tail = None
            while cur:
                if cur.val.key == key:
                    cur.val.value = value
                    return
                else:
                    tail = cur
                    cur = cur.next
            n = Node(p)
            tail.next = n
            tail = n
        else:
            self.__buckets[index] = Node(p)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        if key is None:
            return False
        index = self.__hash(key)
        bucket = self.__buckets[index]
        if bucket:
            cur = bucket
            while cur:
                if cur.val.key == key:
                    return cur.val.value
                cur = cur.next
            return -1
        else:
            return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
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
                if cur.val.key == key:
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


hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
print(hashMap.get(1))
print(hashMap.get(3))
hashMap.put(2, 1)
print(hashMap.get(2))
hashMap.remove(2)
print(hashMap.get(2))
# vim: set expandtab ts=4 sts=4 sw=4 :
