#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-20 23:37:32
# File Name: 217_Contains_Duplicate.py
# Description:
#########################################################################


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        hset = set()
        for n in nums:
            if n in hset:
                return True
            hset.add(n)
        return False


nums = [1, 2, 3, 1]
ret = Solution().containsDuplicate(nums)
print(ret)
# vim: set expandtab ts=4 sts=4 sw=4 :
