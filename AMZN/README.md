# Amazon
- [Amazon](#amazon)
  - [Lc High Frequency Questions](#lc-high-frequency-questions)
  - [Inverview Questions and Follow-Ups](#inverview-questions-and-follow-ups)
    - [OA](#oa)
    - [VO](#vo)
    - [OOD](#ood)

## Lc High Frequency Questions

[121. Best Time to Buy and Sell Stocks](../src/121.best-time-to-buy-and-sell-stock.py)

[239. Sliding Window Maximum *](../src/239.sliding-window-maximum.py)

[721. Account Merge](../src/721.accounts-merge.py)

      Topic:
        Connected Components

      BFS/DFS Algorithm:
        1. Convert input into graph if not
        2. Build adjacent list
              adjacent = {node: [edges]}
        3. seen
              seen = {nodes}
              seen = [False for _ in nodes]
              seen = {node: 0 for node in nodes}
        4. BFS/DFS
      
      DUF algorithm:
        1. Start with disjoint set with all nodes only
        2. For each edge, union two nodes
        3. Return # of sets

[49. Group Anagrams](../src/49.group-anagrams.py)

[472. Concatenated Words](../src/472.concatenated-words.py)

      Topic:
        Word Split/Word Search

      1. DFS
      2. DFS with memorization
      3. DFS + Trie (Todo)
      4. DP (Todo)

[139. Word Break](../src/139.word-break.py)

[140. Word Break II](../src/140.word-break-ii.py)

[1152. Analyze User Website Visit Pattern](../src/1152.analyze-user-website-visit-pattern.py)

[2272. Substring With Largest Variance]

[53. Maximum Subarray]

## Inverview Questions and Follow-Ups
### OA

1. [Find Password Strength](oa1.find-password-strength.py)

   ```
   Given a string password, find the strength of that password. The strength of a password, consisting only lowercase english letters only, is calculated as the sum of the number of distinct characters present in all possible substrings of that password.

   Example:

   Input: password = "good"
   Output: 16

   Input: password = "test"
   Output: 19

   Input: password = "abc"
   Output: 10
   ```

   Follow up:
   - How to solve the problem in O(n) time? DP + dict to save the last index

### VO

1. [Valid Sudoku (Lc 36)](../src/36.valid-sudoku.py)
   
   Follow up:
   - 如果不用list comprehension该怎么写? for loop
   - 判断一行有没有9个不同的数字，用的是python set，如果不准你用这个set，你该怎么写? dict / sort + one iteration
  
2. [Course Schedule (Lc 207)](../src/207.course-schedule.py)

    Follow up:
    - 为什么这个拓扑排序能work？
    - 怎么能输出这个顺序呢？因为解法是拓扑排序，所以这个顺序已经有了，如果用dfs判断是否有环的解法才需要涉及如何保存访问顺序。所以直接print这个顺序就好了。

   Similar:

   [Lc 684. Redundant Connection](../src/684.redundant-connection.py)

3. [Compare Version Numbers (Lc 165)](../src/165.compare-version-numbers.py)

4. [Adding A List of Numbers](vo4.adding-two-numbers.py)

   ```
   Given a list of nodes, where each node represents a number. Calculate the sum of the nodes, and return it as a node. The value of a node is a char, which can be a digit or ‘-’ or ‘+’.

   Example:

   Input:
      ‘-’ -> ‘1’ -> ‘2’ -> ‘4’ (== -124)
      ‘+’ -> ‘1’ (== 1)
      ‘2’ -> ‘5’ (== 25)
   Output: ‘-’ -> ‘9’ -> ‘8’ (== -98)
      -124 + 1 + 25 = -98
   ```

   Similar: 

   [Lc2](../src/2.add-two-numbers.py)

   [Lc445](../src/445.add-two-numbers-ii.py)

5. [Max Ads Profit](vo5.max-ads-profit.py)
   ```
   You will design an algorithm to get max profit by playing ads. There is a limit time and some ads, return the max profit you can get from playing the ads. The Ad must be played completed, and at most once.

   Example:

   Input: Ads = [[68, 20], [30, 15], [40, 20], [50, 25]], where [68, 20] means it is 68 seconds long and will give 20$ profit. Time limit T = 120s.
   Output: The max profit is 60$ (15 + 20 + 25).
   ```

   Follow Up:
   - 如果广告可以play一部分，比如20 seconds的广告只play 10 seconds，得到一半的profit，但是one Ad play at most once, 求最大收益。

6. [Design an Expire Set](vo6.expire-set.py)

   ```
   Design an unbounded Set where each entry has an expriation after the current system time. Implement the following methods:
   - Add/Update
   - Delete
   - Contains
   - Expire: delete expired entries
   ```

   Follow Up:
   - How to handle concurrency requests? 
   - If a user call the contains method, the entry should be deleted but in your design ‍‍‌‌‍‌‌‌‌‍‌‌‍‌‍‍‍‌‍‌it has not been deleted, how to handle?
   这里第二个FU是我用while loop和sleep去删除。我说可以调节sleep的时间，或者用poll直接block住。后来想一下其实在contains被call的时候直接check以及删除就好了....以及多线程写的有点问题。。。

7. [LRU Cache (Lc 146)](../src/146.lru-cache.py)

   Follow up:

   - Race condition issue, 要注意的是只需要锁最小单元
      ```
      Example:
      LRU(3) = [1, 2, 3]
      A: Get(1)                    B: Put(4)
         Check hashmap             check hashmap
         move linked list node     remove head(1)
         return   
      ```
      Solution: 跟你用的data structure有关系。我用的是hashmap+linkedlist设计，所以在get的时候check hashmap不需要锁。 
   
8. [Word Search II (Lc 212)](../src/212.word-search-ii.py)

9. [684. Redundant Connection](../src/684.redundant-connection.py)

Similar: [685. Redundant Connection II](../src/685.redundant-connection-ii.py)
    
10. Meeting Room II

### OOD

1. 设计一个游戏，有很多个岛。然后岛和岛之间有路。user可以选择交通工具，有车和热气球。然后一起从start island出发，每个user每次可以动一步，看谁先走到end island。
按照步骤一点点设计，要有岛，user，和游戏的class。method就自己improvise就行了。这种open-ended的问题只要面试官觉得make sense，应该就差不多了。