#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: Johnny Shi
# Created Time: 2018-08-24 23:13:20
# File Name: add_binary.py
# Description:
#########################################################################
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        len_max = max(len_a, len_b)
        ret = [0] * (len_max + 1)
        i = -1
        add = '0'
        while i >= -len_max:
            if -i <= len_a:
                cur_a = a[i]
            else:
                cur_a = '0'

            if -i <= len_b:
                cur_b = b[i]
            else:
                cur_b = '0'

            if cur_a == '0' and cur_b == '0':
                if add == '1':
                    ret[i] = '1'
                    add = '0'
                else:
                    ret[i] = '0'
            elif (cur_a == '1' and cur_b == '0') or (cur_a == '0' and cur_b == '1'):
                if add == '0':
                    ret[i] = '1'
                else:
                    ret[i] = '0'
                    add = '1'
            else:
                if add == '0':
                    ret[i] = '0'
                else:
                    ret[i] = '1'
                add = '1'
            i -= 1
        if add == '1':
            ret[i] = '1'
            return ''.join(ret)
        else:
            return ''.join(ret[1:])

'''
Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

'''
a = '100'
b = '1'
a = '1010'
b = '1011'
a = '11'
b = '1'
ret = Solution().addBinary(a, b)
print(ret)

# vim: set expandtab ts=4 sts=4 sw=4 :
