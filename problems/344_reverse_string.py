#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-08-25 00:53:16
# File Name: reverse_string.py
# Description:
#########################################################################


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        array_s = list(s)
        array_s.reverse()
        return ''.join(array_s)


s = '123'
s = 'A man, a plan, a canal: Panama'
ret = Solution().reverseString(s)
print(ret)

# vim: set expandtab ts=4 sts=4 sw=4 :
