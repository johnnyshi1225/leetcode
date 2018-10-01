#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-10-01 22:51:49
# File Name: 792_Binary_Search.py
# Description:
#########################################################################


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            n = nums[mid]
            if n == target:
                return mid
            elif n < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


nums = [2, 5]
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(Solution().search(nums, target))
# vim: set expandtab ts=4 sts=4 sw=4 :
