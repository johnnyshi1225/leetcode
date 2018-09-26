#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-26 13:03:44
# File Name: 49_Group_Anagrams.py
# Description:
#########################################################################


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hmap = {}
        for s in strs:
            k = ''.join(sorted(s))
            if k in hmap:
                hmap[k].append(s)
            else:
                hmap[k] = [s]
        return list(hmap.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
# vim: set expandtab ts=4 sts=4 sw=4 :
