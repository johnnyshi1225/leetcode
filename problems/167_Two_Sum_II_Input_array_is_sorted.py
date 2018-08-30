#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-08-29 19:41:05
# File Name: 167_Two_Sum_II_Input_array_is_sorted.py
# Description:
#########################################################################


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers or len(numbers) < 2:
            return []
        small_end = 0
        big_end = len(numbers) - 1
        while small_end < big_end:
            asum = numbers[small_end] + numbers[big_end]
            if asum < target:
                small_end += 1
            elif asum > target:
                big_end -= 1
            else:
                return [small_end + 1, big_end + 1]
        return []


# numbers sorted in ascending order
numbers = [2, 7, 11, 15]
numbers = [-3, 0, 3, 7]
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 9
ret = Solution().twoSum(numbers, target)
print(ret)
# vim: set expandtab ts=4 sts=4 sw=4 :
