#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-08-30 13:20:40
# File Name: 209_Minimum_Size_Subarray_Sum.py
# Description:
#########################################################################


class Solution:
    def minSubArrayLen1(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # 最暴力解法，超时
        min_len = len(nums)
        for i in range(0, len(nums)):
            asum = 0
            for j in range(i, len(nums)):
                asum += nums[j]
                if asum >= s:
                    min_len = min(j - i + 1, min_len)
                    break
                if i == 0 and j == len(nums) - 1:
                    # 遍历了一遍都小于s，不可能出现新的sum >= s的情况了
                    return 0
        return min_len

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l_i = 0
        r_i = 0
        asum = nums[l_i]
        min_len = 0
        while l_i <= r_i and r_i < len(nums):
            if asum < s:
                r_i += 1
                if r_i < len(nums):
                    asum += nums[r_i]
            elif asum >= s:
                if min_len == 0:
                    min_len = r_i - l_i + 1
                else:
                    min_len = min(min_len, r_i - l_i + 1)
                asum -= nums[l_i]
                l_i += 1
        return min_len


s = 7
nums = [2, 3, 1, 2, 4, 3]
print(nums)
ret = Solution().minSubArrayLen(s, nums)
print(ret)
# vim: set expandtab ts=4 sts=4 sw=4 :
