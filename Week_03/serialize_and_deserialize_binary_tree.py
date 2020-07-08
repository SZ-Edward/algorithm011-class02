# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def transform(node):
          if not node:
            res.append('#')
          else:
            res.append(str(node.val))
            transform(node.left)
            transform(node.right)

        transform(root)
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        res = iter(data.split(','))
        def transform():
          val = next(res)
          if val == '#':
            return None
          node = TreeNode(int(val))
          node.left = transform()
          node.right = transform()
          return node

        return transform()
