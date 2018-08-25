#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-08-25 21:15:57
# File Name: rotate_array.py
# Description:
#########################################################################
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        offset = k % n
        if offset == 0:
            return

        i = 0
        tmp = nums[i]
        back = 0  # n 和 offset存在倍数关系时，会出现过程中回到已经swap的位置
        for x in range(0, n):
            i = (i + offset) % n
            nums[i], tmp = tmp, nums[i]
            back = (back + offset) % n
            if back == 0:
                i = (i + 1) % n  # 回到已swap位置，往右走一步
                tmp = nums[i]


nums = [1, 2, 3, 4]
nums = [1, 2, 3, 4, 5, 6, 7]
nums = [1, 2, 3, 4, 5, 6]
k = 3  # k is non-negative
Solution().rotate(nums, k)
print(nums)

# vim: set expandtab ts=4 sts=4 sw=4 :
