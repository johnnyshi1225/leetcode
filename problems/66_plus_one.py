#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-08-27 15:34:39
# File Name: 66_plus_one.py
# Description:
#########################################################################


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        last = 1
        for i in range(1, len(digits) + 1):
            d = digits[-i]
            add = d + last
            if add != 10:
                digits[-i] = add
                last = 0
            else:
                digits[-i] = 0
                last = 1
        if last == 1:
            # digits is not long enough
            digits = [0] * (len(digits) + 1)
            digits[0] = 1

        return digits


digits = [1, 9, 9]
digits = [1, 2, 3]
digits = [9, 9]
digits = [0]
ret = Solution().plusOne(digits)
print(ret)
# vim: set expandtab ts=4 sts=4 sw=4 :
