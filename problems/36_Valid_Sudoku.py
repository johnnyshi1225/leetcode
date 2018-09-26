#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-26 13:12:58
# File Name: 36_Valid_Sudoku.py
# Description:
#########################################################################


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        ROW = 9
        COL = 9
        BLOB = 3
        hset = set()
        for r in range(ROW):
            for c in range(COL):
                n = board[r][c]
                if n != '.':
                    rkey = 'r_{}:{}'.format(r, n)
                    ckey = 'c_{}:{}'.format(c, n)
                    blob_key = 'b_{}_{}:{}'.format(r // BLOB, c // BLOB, n)
                    if rkey in hset or ckey in hset or blob_key in hset:
                        return False
                    hset.add(rkey)
                    hset.add(ckey)
                    hset.add(blob_key)
        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print(Solution().isValidSudoku(board))
# vim: set expandtab ts=4 sts=4 sw=4 :
