# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/plus-one/
"""
def plusOne(digits):
    if len(digits) == 0:
        return [1]
    for each in digits:
        if each > 9:
            return    
    if len(digits) == 1:
        if digits[0] == 9:
            return [1, 0]
        return [digits[0] + 1]

    length = len(digits)
    result = 0
    for each in digits:
        length -= 1
        result += each * (10 ** length)
    result += 1    
    return [int(c) for c in str(result)]
