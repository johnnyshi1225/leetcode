#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-21 13:07:24
# File Name: 202_Happy_Number.py
# Description:
#########################################################################


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result_set = set()
        while n not in result_set:
            result_set.add(n)
            n_sum = 0
            while n != 0:
                num = n % 10
                n_sum += num ** 2
                n //= 10
            n = n_sum
            if n == 1:
                return True
        return False


n = 19
n = 20
print(Solution().isHappy(n))
# vim: set expandtab ts=4 sts=4 sw=4 :
