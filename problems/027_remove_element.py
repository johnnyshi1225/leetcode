#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-08-25 01:36:47
# File Name: remove_element.py
# Description:
#########################################################################


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i


nums = [3, 2, 3, 2, 1]
val = 3
ret = Solution().removeElement(nums, val)
print(ret)
print(nums)

# vim: set expandtab ts=4 sts=4 sw=4 :
