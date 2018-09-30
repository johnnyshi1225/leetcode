#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-30 13:04:11
# File Name: 102_Binary_Tree_Level_Order_Traversal.py
# Description:
#########################################################################


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        level_list = [root]
        while level_list:
            ret.append([])
            origin_len = len(level_list)
            for i in range(origin_len):
                n = level_list.pop(0)
                ret[-1].append(n.val)
                if n.left:
                    level_list.append(n.left)
                if n.right:
                    level_list.append(n.right)
        return ret


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(Solution().levelOrder(root))
# vim: set expandtab ts=4 sts=4 sw=4 :
