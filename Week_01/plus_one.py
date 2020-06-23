# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/plus-one/
"""
def plusOne(digits):
    for i in range(len(digits)):
        if digits[~i] < 9:
            digits[~i] += 1
            return digits
        digits[~i] = 0
    return [1] + [0] * len(digits)
