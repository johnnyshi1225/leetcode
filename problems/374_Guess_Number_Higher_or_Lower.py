#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-10-30 20:25:40
# File Name: 374_Guess_Number_Higher_or_Lower.py
# Description:
#########################################################################


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):


target = 6


def guess(num):
    if num == target:
        return 0
    elif num > target:
        return -1
    else:
        return 1


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            guess_ret = guess(mid)
            if guess_ret == 0:
                return mid
            elif guess_ret == 1:
                left = mid + 1
            else:
                right = mid - 1
        return mid


print(Solution().guessNumber(10))
# vim: set expandtab ts=4 sts=4 sw=4 :
