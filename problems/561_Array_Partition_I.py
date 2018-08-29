#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-08-29 17:31:13
# File Name: Array_Partition.py
# Description:
#########################################################################


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        all_sum = 0
        for i in range(0, len(nums), 2):
            all_sum += nums[i]
        return all_sum


nums = [1, 2, 3, 4]
ret = Solution().arrayPairSum(nums)
print(ret)
# vim: set expandtab ts=4 sts=4 sw=4 :
