# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/word-pattern/
"""
def wordPattern(pattern, str):
    word = str.split()
    return list(map(pattern.index, pattern)) == list(map(word.index, word))
