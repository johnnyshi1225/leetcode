#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-21 13:00:30
# File Name: 349_Intersection_of_Two_Arrays.py
# Description:
#########################################################################


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        hset = set(nums1)
        ret = hset.intersection(set(nums2))
        return list(ret)


nums1 = [1, 2, 3]
nums2 = [3, 3, 4]
print(Solution().intersection(nums1, nums2))
# vim: set expandtab ts=4 sts=4 sw=4 :
