## 算法训练营 第三周（7.6-7.12）学习小结

本周学习递归、分治、回溯，其实就是递归，解决重复性的问题，而分治和回溯的出现是解决一些需要问题分割的特殊递归问题，本质还是递归的问题。

#### 一、递归
自己调用自己，一个问题可以分解成同样的子问题

```
def recursion(level, params):
    # terminator
    if level > MAX_LEVEL:
        # process result
        return
    
    # process current logic
    process(level, params)

    # drill down
    recursion(level + 1, params)
    
    # reverse status

```

#### 二、分治
将一个规模为N的问题分解为K个规模较小的子问题，这些子问题相互独立且与原问题性质相同。求出子问题的解，就可得到原问题的解。

```
def divide_conquer(problem, param1, param2, ...): 
    # recursion terminator 
    if not problem: 
        print_result 
	return
 
    # prepare data 
    data = prepare_data(problem) 
    subproblems = split_problem(problem, data) 

    # conquer subproblems 
    subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
    subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
    subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
    …

    # process and generate the final result 
    result = process_result(subresult1, subresult2, subresult3, …)
	
    # revert the current level states

```

#### 三、回溯
一种不断“试错”的暴力搜索法，它尝试分步的去解决一个问题。在分步解决问题的过程中，当它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚至是上几步的计算，再通过其它的可能的分步解答再次尝试寻找问题的答案。

```
def backtrack(path, choices):
    if condition:
        result.append(path)
        return

    for each in choices:
        # make choice
        backtrack(path, choices)
        # withdraw choice
```
