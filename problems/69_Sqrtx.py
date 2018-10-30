#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-10-30 20:07:06
# File Name: 69_Sqrtx.py
# Description:
#########################################################################
import math


class Solution:
    def mySqrt1(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = math.sqrt(x)
        return int(math.floor(ret))

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if (mid * mid) <= x:
                left = mid + 1
                ret = mid
            else:
                right = mid - 1
        return ret


print(Solution().mySqrt(8))
# vim: set expandtab ts=4 sts=4 sw=4 :
