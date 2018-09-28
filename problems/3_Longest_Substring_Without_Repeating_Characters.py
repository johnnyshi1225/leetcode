#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-28 21:26:10
# File Name: 3_Longest_Substring_Without_Repeating_Characters.py
# Description:
#########################################################################


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        for i, c in enumerate(s):
            length = 0
            cset = set()
            cset.add(c)
            length += 1
            for j in range(i + 1, len(s)):
                if s[j] not in cset:
                    cset.add(s[j])
                    length += 1
                else:
                    break
            max_length = max(max_length, length)
        return max_length


print(Solution().lengthOfLongestSubstring('abcabcbb'))
print(Solution().lengthOfLongestSubstring('ssssss'))
print(Solution().lengthOfLongestSubstring('pwwkew'))
# vim: set expandtab ts=4 sts=4 sw=4 :
