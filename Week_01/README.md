## 算法训练营 第一周（6.22-6.28）学习小结

#### 一、分析 Queue 和 Priority Queue 的源码
Queue 和 Priority Queue 分别是队列和优先级队列，它们的区别在于：队列是先入先出（FIFO）的数据结构，你可以想象为超市收银台前等待结账的排队人群，如果想要结账，你必须在队伍的末尾加入队伍（入队），排到谁了谁就可以买单离开（出队）；而优先级队列不是这样的，在你加入队伍后（入队），队伍中的人根据“优先级”到收银台前买单离开（出队）。这里的“优先级”可以是超市的会员卡等级，比如张三排在李四的前面，张三是超市的 VIP，李四是超市的 SVIP，那么李四就可以在张三的前面买单离开。优先级队列就是这样一种自带优先级的数据结构，你也可以认为这种优先级是一种排序。

理解了队列和优先级队列这两种数据结构，再来看 Java 实现就容易了。Queue 的 Java API 提供了两套操作队列的方法，每一套方法都有队列的基本操作，入队、出队和查找队列元素。它们的区别是 add / remove / element 这套方法执行失败会抛异常，而 offer / poll / peek 这套方法是返回特殊值。

PriorityQueue 的 Java API 同样提供了入队 add/offer、出队 remove/clear、查找队列元素 contains 的方法。除此之外需要注意的是 comparator，前面说到优先级队列的时候说过“优先级其实是一种排序”，我们的优先级队列是如何排“优先级”的呢？就是 comparator 起的作用。

#### 二、用 add first 或 add last 这套新的 API 改写 Deque 的代码
```
import java.util.Deque;
import java.util.LinkedList;

public static void main(String[] args) {
    Deque<String> deque = new LinkedList<String>();
    deque.addFirst("a"); 
    deque.addFirst("b");
    deque.addFirst("c");
    System.out.println(deque);

    String str = deque.peekFirst();
    System.out.println(str); 
    System.out.println(deque);

    while (deque.size() > 0) {
        System.out.println(deque.removeFirst());
    }
    System.out.println(deque);
}
```

#### 三、五毒神掌刷题套路
五毒神掌是覃超老师总结的刷题套路，leetcode 上面的算法题最少刷五遍。

第一遍：读题和思考。
如果五分钟内没有思路，马上看题解，看别人是怎么解题的。
如果有思路，写下来，比较自己和别人解法的优劣。
学习别人写得好的地方，背诵、默写（形成肌肉记忆）。

第二遍：自己写，提交 leetcode。

第三遍：24小时后重复练习，熟悉不同的解法。

第四遍：一周后再次练习。

第五遍：面试前一周恢复性训练。

#### 四、第一周的学习感受
第一周学习了【数组、链表、跳表】和【栈、队列、优先队列、双端队列】，视频里覃超老师介绍了这些数据结构以及常用操作和对应的时间复杂度。由于我有一些基础，所以理解起来不难，但是在做作业的时候，特别是链表相关的题目，引用来回传递，人都搞懵了。希望有个机会老师再讲讲这方面的题。

这一周做了不少题目，比我以前一个人刷 leetcode 效率高多了。个人感觉五毒神掌这个刷题套路很有用，是一种刻意练习的学习方法，也不止于可以用来刷算法。我用一个笔记本专门记录用五毒神掌刷过的题目，目前第一周只进行到第三遍，已经有15道题了。这里我有一个问题：如果一道题目有多个解法，我要把不同的解法都记下来吗？还是说选一个自己能记住的最优解法就可以了？

现在每天都会刷题在群里打卡，但是大家打卡就没了，其实希望有一个定期 code review 的活动，互相评审代码，精进写代码的能力。
