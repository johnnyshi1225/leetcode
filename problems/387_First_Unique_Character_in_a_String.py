#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-24 10:50:54
# File Name: 387_First_Unique_Character_in_a_String.py
# Description:
#########################################################################


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1


s = 'loveleetcode'
s = 'aaabbbcccc'
print(Solution().firstUniqChar(s))
# vim: set expandtab ts=4 sts=4 sw=4 :
