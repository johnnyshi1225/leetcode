#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-29 21:32:07
# File Name: 94_Binary_Tree_Inorder_Traversal.py
# Description:
#########################################################################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = self._inorder_sub(root)
        return ret

    def _inorder_sub(self, node):
        ret = []
        if node:
            ret += self._inorder_sub(node.left)
            ret.append(node.val)
            ret += self._inorder_sub(node.right)
        return ret
# vim: set expandtab ts=4 sts=4 sw=4 :
