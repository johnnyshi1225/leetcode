#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-23 22:00:43
# File Name: 205_Isomorphic_Strings.py
# Description:
#########################################################################


class Solution:
    def isIsomorphic1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_map = self._get_stats(s)
        t_map = self._get_stats(t)
        for i in range(len(s)):
            if s_map[s[i]] != t_map[t[i]]:
                return False
        return True

    def _get_stats(self, string):
        hmap = {}
        for i in range(len(string)):
            c = string[i]
            if c in hmap:
                hmap[c].append(i)
            else:
                hmap[c] = [i]
        return hmap

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_hmap = {}
        t_hmap = {}
        for i in range(len(s)):
            if s[i] not in s_hmap:
                s_hmap[s[i]] = t[i]
            elif s_hmap[s[i]] != t[i]:
                return False
            if t[i] not in t_hmap:
                t_hmap[t[i]] = s[i]
            elif t_hmap[t[i]] != s[i]:
                return False
        return True


s = 'apple'
t = 'xcceq'
s = 'ab'
t = 'aa'
s = 'egg'
t = 'app'
print(Solution().isIsomorphic(s, t))
# vim: set expandtab ts=4 sts=4 sw=4 :
