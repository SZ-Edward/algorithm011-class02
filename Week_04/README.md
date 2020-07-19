## 算法训练营 第四周（7.13-7.19）学习小结

本周学习深度优先遍历、广度优先遍历、贪心算法、二分查找。

#### 一、深度优先搜索（DFS）和广度优先搜索（BFS）
在树或图里搜索特定节点
  - 每个节点仅访问一次
  - 对于节点的不同访问顺序，有：
    - 深度优先搜索 Depth First Search
    - 广度优先搜索 Breadth First Search
    - 其他：优先级优先搜索

```
# 深度优先搜索（DFS）的递归写法
visited = set() 

def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 

    visited.add(node) 

    # process current node here. 
    ...
    for next_node in node.children(): 
        if next_node not in visited: 
	    dfs(next_node, visited)
```

```
# 深度优先搜索（DFS）的非递归写法
def DFS(self, tree): 
    if tree.root is None: 
	return [] 

    visited, stack = [], [tree.root]

    while stack: 
	node = stack.pop() 
	visited.add(node)

	process (node) 
	nodes = generate_related_nodes(node) 
	stack.push(nodes) 

    # other processing work 
    ...
```

```
# 广度优先搜索（BFS）
def BFS(graph, start, end):
    visited = set()
    queue = [] 
    queue.append([start]) 

    while queue: 
	node = queue.pop() 
	visited.add(node)
		
        process(node) 
	nodes = generate_related_nodes(node) 
	queue.push(nodes)
	
    # other processing work 
    ...
```


#### 二、贪心算法
贪心算法是一种在当下每一步中选择最好或者最优的选择，从而你导致的结果是全局最好或最优。

贪心算法和动态规划的异同点：
   - 贪心：对于每个子问题的解决方案都作出选择，且不能回退
   - 动态规划：会保存以前的没个结果，并会根据以前的结果对当前选择，有回退功能
   - 回溯：能回退


#### 三、二分查找
使用二分查找的前提条件
   - 目标函数单调性（单调递增或单调递减）
   - 存在上下界（bounded）
   - 可以通过索引访问元素 (index accessible)

```
left, right = 0, len(array) - 1 
while left <= right: 
    mid = (left + right) / 2 
    if array[mid] == target: 
        # find the target!! 
        break or return result 
    elif array[mid] < target: 
        left = mid + 1 
    else: 
        right = mid - 1
```
