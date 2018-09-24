#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-24 08:46:46
# File Name: 599_Minimum_Index_Sum_of_Two_Lists.py
# Description:
#########################################################################


class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        hmap = {}
        ret_map = {}
        for i in range(len(list1)):
            hmap[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in hmap:
                isum = i + hmap[list2[i]]
                if isum not in ret_map:
                    ret_map[isum] = [list2[i]]
                else:
                    ret_map[isum].append(list2[i])
        isums = list(ret_map.keys())
        isums.sort()
        return ret_map[isums[0]]


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]
print(Solution().findRestaurant(list1, list2))
# vim: set expandtab ts=4 sts=4 sw=4 :
