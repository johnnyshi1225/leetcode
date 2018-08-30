#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-08-30 13:08:45
# File Name: 485_Max_Consecutive_Ones.py
# Description:
#########################################################################


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_count = 0
        for num in nums:
            if num == 1:
                count += 1
            elif num == 0:
                if count > max_count:
                    max_count = count
                count = 0
        if count > max_count:
            max_count = count
        return max_count


nums = [1, 1, 0, 1, 1, 1]
ret = Solution().findMaxConsecutiveOnes(nums)
print(ret)
# vim: set expandtab ts=4 sts=4 sw=4 :
