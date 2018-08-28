#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-08-28 12:37:54
# File Name: 14_Longest_Common_Prefix.py
# Description:
#########################################################################


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        commonChars = []
        lastCommonChar = ''
        curIndex = 0
        while True:
            for s in strs:
                if len(s) > curIndex:
                    c = s[curIndex]
                    if not lastCommonChar:
                        lastCommonChar = c
                    elif c != lastCommonChar:
                        return ''.join(commonChars)
                else:
                    return ''.join(commonChars)
            commonChars.append(c)
            curIndex += 1
            lastCommonChar = ''


strs = ["flower", "flow", "flight"]
strs = ["dog", "racecar", "car"]
ret = Solution().longestCommonPrefix(strs)
print(ret)
# vim: set expandtab ts=4 sts=4 sw=4 :
