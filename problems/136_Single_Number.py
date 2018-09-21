#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-21 12:42:01
# File Name: 136_Single_Number.py
# Description:
#########################################################################


class Solution:
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hset = set()
        for n in nums:
            if n in hset:
                hset.remove(n)
            else:
                hset.add(n)
        if hset:
            return hset.pop()

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for n in nums:
            ret ^= n
        return ret


nums = [1, 2, 3, 2, 1]
print(Solution().singleNumber(nums))
# vim: set expandtab ts=4 sts=4 sw=4 :
