#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-27 20:42:13
# File Name: 652_Find_Duplicate_Subtrees.py
# Description:
#########################################################################


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findDuplicateSubtrees1(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        ret = []
        self.hmap = {}  # <preorder-sub:node>
        self._preorder_sub(root)
        for k, v in self.hmap.items():
            if len(v) > 1:
                ret.append(v[0])
        return ret

    def _preorder_sub1(self, node):
        ret = []
        if node:
            ret.append(str(node.val))
            left_sub = self._preorder_sub(node.left)
            right_sub = self._preorder_sub(node.right)
            ret += left_sub
            ret += right_sub
            if left_sub != ['-']:
                k = ','.join(left_sub)
                self.hmap[k] = self.hmap.get(k, [])
                self.hmap[k].append(node.left)
            if right_sub != ['-']:
                k = ','.join(right_sub)
                self.hmap[k] = self.hmap.get(k, [])
                self.hmap[k].append(node.right)
        if not ret:
            ret = ['-']
        return ret

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.ret = []
        self.hmap = {}  # <preorder-sub:node>
        self._preorder_sub(root)
        print(self.hmap)
        return self.ret

    def _preorder_sub(self, node):
        if not node:
            return '-'
        k = '{},{},{}'.format(node.val, self._preorder_sub(node.left), self._preorder_sub(node.right))
        self.hmap[k] = self.hmap.get(k, 0) + 1
        if self.hmap[k] == 2:
            self.ret.append(node)
        return k


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(4)
print(Solution().findDuplicateSubtrees(root))
# vim: set expandtab ts=4 sts=4 sw=4 :
