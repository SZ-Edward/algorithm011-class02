# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/min-stack/
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.data.append(x)
        self.min_stack.append(min(self.min_stack[-1], x))

    def pop(self) -> None:
        self.data.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
