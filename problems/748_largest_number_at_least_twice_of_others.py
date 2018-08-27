#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-08-27 14:26:16
# File Name: 748_largest_number_at_least_twice_of_others.py
# Description:
#########################################################################


class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        max_index = 0
        max_num = 0
        lease_max_num = 0
        for i in range(len(nums)):
            cur = nums[i]
            if cur > max_num:
                lease_max_num = max_num
                max_num = cur
                max_index = i
            elif cur > lease_max_num:
                lease_max_num = cur
        if lease_max_num != 0 and max_num / lease_max_num >= 2:
            return max_index
        elif max_num != 0 and lease_max_num == 0:
            return max_index
        else:
            return -1


nums = [0, 0, 0]
nums = [1, 2, 3, 4]
nums = [3, 6, 1, 0]
nums = [1]
ret = Solution().dominantIndex(nums)
print(ret)

# vim: set expandtab ts=4 sts=4 sw=4 :
