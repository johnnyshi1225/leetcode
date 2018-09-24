#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-09-24 08:46:46
# File Name: 599_Minimum_Index_Sum_of_Two_Lists.py
# Description:
#########################################################################
import sys


class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        hmap = {}
        min_sum = sys.maxsize
        min_list = []
        for i in range(len(list1)):
            hmap[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in hmap:
                isum = i + hmap[list2[i]]
                if isum < min_sum:
                    min_sum = isum
                    min_list = [list2[i]]
                elif isum == min_sum:
                    min_list.append(list2[i])
        return min_list


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list1 = ["Shogun", "KFC", "Tapioca Express", "Burger King"]
list2 = ["KFC", "Shogun", "Burger King"]
print(Solution().findRestaurant(list1, list2))
# vim: set expandtab ts=4 sts=4 sw=4 :
