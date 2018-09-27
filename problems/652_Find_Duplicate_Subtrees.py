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
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

    def _get_children(self, node):
        children = []


# vim: set expandtab ts=4 sts=4 sw=4 :
