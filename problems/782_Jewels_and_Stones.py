#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-28 21:18:01
# File Name: 782_Jewels_and_Stones.py
# Description:
#########################################################################


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ret = 0
        if not J or not S:
            return ret
        jewel_set = set()
        for c in J:
            jewel_set.add(c)
        for c in S:
            if c in jewel_set:
                ret += 1
        return ret


J = 'aA'
S = 'aAAbbbb'
print(Solution().numJewelsInStones(J, S))
# vim: set expandtab ts=4 sts=4 sw=4 :
