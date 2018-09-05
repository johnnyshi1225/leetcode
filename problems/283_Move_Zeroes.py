#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-05 19:58:31
# File Name: 283_Move_Zeroes.py
# Description:
#########################################################################


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []

        last_index = 0
        for i in range(len(nums)):
            n = nums[i]
            if n != 0:
                if nums[last_index] == 0:
                    nums[last_index], nums[i] = nums[i], nums[last_index]
                last_index += 1


nums = [0, 1, 0, 3, 12]
nums = [0, 0, 0, 3, 12]
nums = [1, 2, 0, 4, 0, 5, 6]
ret = Solution().moveZeroes(nums)
print(nums)
# vim: set expandtab ts=4 sts=4 sw=4 :
