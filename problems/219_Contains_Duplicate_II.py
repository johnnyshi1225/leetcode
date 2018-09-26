#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-26 12:40:57
# File Name: 219_Contains_Duplicate_II.py
# Description:
#########################################################################


class Solution:
    def containsNearbyDuplicate1(self, nums, k):
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
                if hmap[nums[i]][-1] - hmap[nums[i]][-2] <= k:
                    return True
            else:
                hmap[nums[i]] = [i]
        return False

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        hmap = {}
        for i, n in enumerate(nums):
            if n in hmap:
                if i - hmap[n] <= k:
                    return True
            hmap[n] = i
        return False


nums = [1, 0, 1, 1]
k = 1
nums = [1, 2, 3, 1]
k = 3
print(Solution().containsNearbyDuplicate(nums, k))
# vim: set expandtab ts=4 sts=4 sw=4 :
