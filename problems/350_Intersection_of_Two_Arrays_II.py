#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-25 23:22:02
# File Name: 350_Intersection_of_Two_Arrays_II.py
# Description:
#########################################################################


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        ret = []
        map1 = self._count(nums1)
        map2 = self._count(nums2)
        for k, v in map1.items():
            if k in map2:
                ret += [k] * min(v, map2[k])
        return ret

    def _count(self, nums):
        hmap = {}
        for n in nums:
            if n in hmap:
                hmap[n] += 1
            else:
                hmap[n] = 1
        return hmap


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(Solution().intersect(nums1, nums2))
# vim: set expandtab ts=4 sts=4 sw=4 :
