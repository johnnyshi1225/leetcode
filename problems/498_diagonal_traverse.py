#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-08-24 14:19:16
# File Name: diagonal_traverse.py
# Description:
#########################################################################


class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m = len(matrix)
        n = 0
        if m:
            n = len(matrix[0])
        else:
            return []

        ret = [0] * (m * n)
        i = 1
        j = -1
        next_offset = [(-1, 1), (1, -1)]
        cur_next = 0
        for index in range(0, m * n):
            # move to next
            i += next_offset[cur_next][0]
            j += next_offset[cur_next][1]

            if j >= n:
                # 上角
                i += 2
                j = n - 1
                cur_next = 1
            elif i >= m:
                # 下角
                i = m - 1
                j += 2
                cur_next = 0
            elif i < 0:
                i = 0
                cur_next = 1
            elif j < 0:
                j = 0
                cur_next = 0
            print(index, i, j)
            ret[index] = matrix[i][j]

        return ret


matrix = [[]]
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
matrix = [
    [1, 2],
    [3, 4]
]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
ret = Solution().findDiagonalOrder(matrix)
print(ret)

# vim: set expandtab ts=4 sts=4 sw=4 :
