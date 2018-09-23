#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-23 21:47:31
# File Name: 1_Two_Sum.py
# Description:
#########################################################################


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}
        for i in range(len(nums)):
            hmap[nums[i]] = i

        for i in range(len(nums)):
            j = target - nums[i]
            if hmap.get(j) is not None and i != hmap[j]:
                return [i, hmap[j]]


nums = [2, 7, 8, 9]
nums = [2, 7, 8, 9]
target = 4
print(Solution().twoSum(nums, target))
# vim: set expandtab ts=4 sts=4 sw=4 :
