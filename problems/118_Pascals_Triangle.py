#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-08-27 17:38:42
# File Name: 118_pascal_s_triangle.py
# Description:
#########################################################################


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        for n in range(numRows):
            if n == 0:
                ret.append([1])
                continue

            new = [0] * (n + 1)
            new[0] = 1
            new[-1] = 1
            for i in range(1, n):
                new[i] = ret[n - 1][i - 1] + ret[n - 1][i]
            ret.append(new)

        return ret


numRows = 5
numRows = 15
ret = Solution().generate(numRows)
for row in ret:
    print(row)
# vim: set expandtab ts=4 sts=4 sw=4 :
