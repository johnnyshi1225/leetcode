#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-08-24 13:39:25
# File Name: find_pivot_index.py
# Description:
#########################################################################
class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return -1

        i = 0
        sum_left = 0
        sum_right = sum(nums[i + 1:])
        while i < len(nums):
            if sum_left == sum_right:
                return i
            else:
                sum_left += nums[i]
                i += 1
                if i == len(nums):
                    return -1
                sum_right -= nums[i]
        return -1


nums = []
nums = [1, 2]
nums = [1, 7, 3, 6, 5, 6]
nums = [-1, 2, 3, 1, 4]
nums = [-1, -1, 0, 1, 1, 0]
solution = Solution()
ret = solution.pivotIndex(nums)
print(ret)

# vim: set expandtab ts=4 sts=4 sw=4 :
