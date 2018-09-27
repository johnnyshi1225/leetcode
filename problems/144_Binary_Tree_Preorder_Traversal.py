#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-27 21:45:29
# File Name: 144_Binary_Tree_Preorder_Traversal.py
# Description:
#########################################################################


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = self._preorder_sub(root)
        return ret

    def _preorder_sub(self, node):
        ret = []
        if node:
            ret.append(node.val)
            ret += self._preorder_sub(node.left)
            ret += self._preorder_sub(node.right)
        return ret


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(Solution().preorderTraversal(root))
# vim: set expandtab ts=4 sts=4 sw=4 :
