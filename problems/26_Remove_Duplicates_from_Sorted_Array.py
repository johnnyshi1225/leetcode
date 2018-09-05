#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-03 17:42:24
# File Name: 26_Remove_Duplicates_from_Sorted_Array.py
# Description:
#########################################################################


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        last_num = None
        last_index = None
        for i in range(len(nums)):
            n = nums[i]
            if last_num is None:
                last_num = n
                last_index = i
            elif n == last_num:
                continue
            else:
                # new number
                last_index += 1
                last_num = n
                nums[last_index] = last_num

        return last_index + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
ret = Solution().removeDuplicates(nums)
print(ret)
print(nums)
# vim: set expandtab ts=4 sts=4 sw=4 :
