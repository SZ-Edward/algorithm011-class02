# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
"""
class Solution(object):
    def letterCombinations(self, digits):
        if not digits or len(digits) == 0:
          return []

        map = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        res = []

        def combinations(string, level, digits, map):
          if len(digits) == len(string):
            res.append(string)
            return
          letter = map.get(digits[level])
          for i in range(len(letter)):
            combinations(string + letter[i], level + 1, digits, map)

        combinations('', 0, digits, map)
        return res
