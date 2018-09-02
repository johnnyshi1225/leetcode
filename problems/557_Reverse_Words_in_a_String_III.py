#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-02 00:28:04
# File Name: 557_Reverse_Words_in_a_String_III.py
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
        for i in range(len(l)):
            l[i] = l[i][::-1]
        return ' '.join(l)


s = "Let's take LeetCode contest"
ret = Solution().reverseWords(s)
print(ret)
# vim: set expandtab ts=4 sts=4 sw=4 :
