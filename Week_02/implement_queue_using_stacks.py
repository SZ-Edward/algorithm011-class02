# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/implement-queue-using-stacks/
"""
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.in_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.move()
        return self.out_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.move()
        return self.out_stack[-1]        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return (not self.in_stack) and (not self.out_stack)

    def move(self) -> None:
      if not self.out_stack:
        while self.in_stack:
          self.out_stack.append(self.in_stack.pop())
