#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-08-31 22:05:28
# File Name: 119_Pascals_Triangle_II.py
# Description:
#########################################################################


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = []
        for n in range(rowIndex + 1):
            if n == 0:
                ret.append([1])
                continue

            new = [0] * (n + 1)
            new[0] = 1
            new[-1] = 1
            for i in range(1, n):
                new[i] = ret[n - 1][i - 1] + ret[n - 1][i]
            ret.append(new)

        return ret[rowIndex]


rowIndex = 3
ret = Solution().getRow(rowIndex)
print(ret)
# vim: set expandtab ts=4 sts=4 sw=4 :
