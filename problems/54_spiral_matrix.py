#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-08-27 16:30:28
# File Name: 54_spiral_matrix.py
# Description:
#########################################################################


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        ret = [0] * (m * n)
        up_edge = 0
        right_edge = n - 1
        down_edge = m - 1
        left_edge = 0
        i = 0
        j = -1
        direct = (0, 1)

        for x in range(0, len(ret)):
            i += direct[0]
            j += direct[1]

            if left_edge <= j <= right_edge and up_edge <= i <= down_edge:
                pass
            elif j > right_edge:
                j = right_edge
                i += 1
                direct = (1, 0)
                up_edge += 1
            elif i > down_edge:
                i = down_edge
                j -= 1
                direct = (0, -1)
                right_edge -= 1
            elif j < left_edge:
                j = left_edge
                i -= 1
                direct = (-1, 0)
                down_edge -= 1
            elif i < up_edge:
                i = up_edge
                j += 1
                direct = (0, 1)
                left_edge += 1
            ret[x] = matrix[i][j]

        return ret


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
matrix = [
    [],
]
ret = Solution().spiralOrder(matrix)
print(ret)
# vim: set expandtab ts=4 sts=4 sw=4 :
