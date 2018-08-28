#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-08-27 17:51:50
# File Name: 28_Implement_strStr.py
# Description:
#########################################################################


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None:
            return -1
        if needle == '':
            return 0
        return haystack.find(needle)


haystack = 'this is a simple string'
needle = 'is'
ret = Solution().strStr(haystack, needle)
print(ret)
# vim: set expandtab ts=4 sts=4 sw=4 :
