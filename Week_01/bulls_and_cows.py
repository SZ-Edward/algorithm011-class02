# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/bulls-and-cows/
"""
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        sh = defaultdict(int)
        gh = defaultdict(int)

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                sh[s] += 1
                gh[g] += 1      
 
        cows = sum(min(sh[key], gh[key]) for key in sh)
        return f"{bulls}A{cows}B"
