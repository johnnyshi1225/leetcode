#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-05 21:38:46
# File Name: 838_Design_Linked_List.py
# Description:
#########################################################################


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        node = self.__get(index)
        if node:
            return node.val
        else:
            return -1

    def __get(self, index):
        """
        Get the node of the index-th node in the linked list. If the index is invalid, return None.
        :type index: int
        :rtype: Node
        """
        if index > self.length - 1:
            return None

        if index < self.length / 2:
            # start from head
            cur = self.head
            for i in range(index):
                cur = cur.next
        else:
            # start from tail
            cur = self.tail
            for i in range(self.length - 1 - index):
                cur = cur.prev

        return cur

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.length += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.length += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == self.length:
            self.addAtTail(val)
        else:
            cur = self.__get(index)
            if cur:
                node = Node(val)
                node.next = cur
                node.prev = cur.prev
                node.prev.next = node
                cur.prev = node
                self.length += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        cur = self.__get(index)
        if cur:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            self.length -= 1
            del cur

    def __str__(self):
        ret = []
        cur = self.head
        while cur is not None:
            ret.append(str(cur.val))
            cur = cur.next
        return '->'.join(ret)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


linkedList = MyLinkedList()
linkedList.addAtHead(1)
linkedList.addAtTail(3)
print(linkedList)
linkedList.addAtIndex(1, 2)  # linked list becomes 1->2->3
print(linkedList)
print(linkedList.get(1))            # returns 2
linkedList.deleteAtIndex(1)  # now the linked list is 1->3
print(linkedList)
print(linkedList.get(1))            # returns 3

# vim: set expandtab ts=4 sts=4 sw=4 :
