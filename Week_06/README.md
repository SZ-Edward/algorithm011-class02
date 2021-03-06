## 算法训练营 第六周（7.27-8.2）学习小结

#### 动态规划
动态规划 Dynamic programming，简称DP，通过把原问题分解为相对简单的子问题的方式求解复杂问题的方法。

动态规划在查找有很多重叠子问题的情况的最优解时有效。它将问题重新组合成子问题。为了避免多次解决这些子问题，它们的结果都逐渐被计算并被保存，从简单的问题直到整个问题都被解决。因此，动态规划保存递归时的结果，因而不会在解决同样的问题时花费时间。

动态规划只能应用于有最优子结构的问题。最优子结构的意思是局部最优解能决定全局最优解（对有些问题这个要求并不能完全满足，故有时需要引入一定的近似）。简单地说，问题能够分解成子问题来解决。

动态规划的适用情况：
   - 最优子结构性质。
   - 无后效性。
   - 子问题重叠性质。


解题模版：
   1. 重复子问题
   2. 状态定义
   3. DP 方程
