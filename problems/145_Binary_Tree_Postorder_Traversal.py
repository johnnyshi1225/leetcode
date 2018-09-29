#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-29 21:34:57
# File Name: 145_Binary_Tree_Postorder_Traversal.py
# Description:
#########################################################################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = self._postorder_sub(root)
        return ret

    def _postorder_sub(self, node):
        ret = []
        if node:
            ret += self._postorder_sub(node.left)
            ret += self._postorder_sub(node.right)
            ret.append(node.val)
        return ret
        
# vim: set expandtab ts=4 sts=4 sw=4 :
