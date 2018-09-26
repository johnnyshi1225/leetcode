#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-26 12:40:57
# File Name: 219_Contains_Duplicate_II.py
# Description:
#########################################################################


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        hmap = {}
        for i in range(len(nums)):
            if nums[i] in hmap:
                hmap[nums[i]].append(i)
            else:
                hmap[nums[i]] = [i]
        for _, v in hmap.items():
            if len(v) > 1:
                i = 0
                while i < len(v) - 1:
                    if v[i + 1] - v[i] <= k:
                        return True
                    i += 1
        return False


nums = [1, 2, 3, 1]
k = 3
nums = [1, 0, 1, 1]
k = 1
print(Solution().containsNearbyDuplicate(nums, k))
# vim: set expandtab ts=4 sts=4 sw=4 :
