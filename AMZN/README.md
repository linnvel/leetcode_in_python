# Amazon

## OA

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

## Interview

1. [Valid Sudoku (Lc 36)](../src/36.valid-sudoku.py)
   
   Follow up:
   - 如果不用list comprehension该怎么写? for loop
   - 判断一行有没有9个不同的数字，用的是python set，如果不准你用这个set，你该怎么写? dict / sort + one iteration
  
2. [Course Schedule (Lc 207)](../src/207.course-schedule.py)

    Follow up:
    - 为什么这个拓扑排序能work？
    - 怎么能输出这个顺序呢？因为解法是拓扑排序，所以这个顺序已经有了，如果用dfs判断是否有环的解法才需要涉及如何保存访问顺序。所以直接print这个顺序就好了。

3. [Compare Version Numbers (Lc 165)](../src/165.compare-version-numbers.py)

4. Adding A List of Numbers

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

[Lc445]