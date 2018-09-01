#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-01 22:25:19
# File Name: Reverse_Words_in_a_String.py
# Description:
#########################################################################


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        l = s.split()
        l = l[::-1]
        return ' '.join(l)


s = 'the sky is blue'
ret = Solution().reverseWords(s)
print(ret)
# vim: set expandtab ts=4 sts=4 sw=4 :
