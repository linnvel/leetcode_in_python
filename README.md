# Leetcode Notes

- [Leetcode Notes](#leetcode-notes)
  - [1. Backtracking](#1-backtracking)
    - [1.1 Selected Questions](#11-selected-questions)
    - [1.2 Backtracking Template](#12-backtracking-template)
  - [2. Binary Tree & Divide Conquer](#2-binary-tree--divide-conquer)
    - [2.1 Selected Questions](#21-selected-questions)
    - [2.2 Recursion in Binary Tree](#22-recursion-in-binary-tree)
    - [2.3 Time Complexity Analysis](#23-time-complexity-analysis)
  - [3. Binary Search](#3-binary-search)
    - [3.1 Selected Questions](#31-selected-questions)
    - [3.2 Binary Search Template](#32-binary-search-template)
  - [4. BFS](#4-bfs)
    - [4.1 Selected Questions](#41-selected-questions)
    - [4.2 BFS Template](#42-bfs-template)
  - [5. DFS](#5-dfs)
    - [5.1 Selected Questions](#51-selected-questions)

---

## 1. Backtracking

<br/>

### 1.1 Selected Questions

<br/>

[78. Subsets](src/78.subsets.py)

[90. Subsets II](src/90.subsets-ii.py)

[46. Premutation](src/46.permutations.py)

[47. Permutation II *](src/47.permutations-ii.py)

[39. Combination Sum](src/39.combination-sum.py)

[40. Combination Sum II](src/40.combination-sum-ii.py)

[216. Combination Sum III](src/216.combination-sum-iii.py)

[131. Palindrome Partitioning *](src/131.palindrome-partitioning.py)

[17. Letter Combination of a Phone Number](src/17.letter-combinations-of-a-phone-number.py)

[93. Restore IP Address](src/93.restore-ip-addresses.py)

698 Partition to K Equal Sum Subsets ***

[22. Generate Parentheses](src/22.generate-parentheses.py)

[79. Word Search](src/79.word-search.py)

<br/>

### 1.2 Backtracking Template

<br/>
    
```python
def helper(input, results, cur, startIndex):
    if return_condition:
        results.append(cur[:])  # deep copy
        return
    for i in range(startIndex, len(input)):
        if continue_condition:
            continue
        update startIndex
        update cur
        helper(input, results, cur, startIndex)
        recover cur  # backtracking

def mainFunction(input):
    results = []
    cur = []
    helper(input, results, cur, 0)
    return results
```

Notes:

1. How to update `startIndex`?
    
    Objective: distinguish two adjacent recursion 
    
    - `startIndex := i + 1`
        - `cur` has all or part of elements in `input`. Each element appears **at most once**.
        - Subsets I/II, Palindrome Partitioning, Restore IP Address
    - `startIndex := i`
        - `cur` has all or part of elements in `input`. Each element could appear **multiple times**.  
        - Combination Sum
    - `seen`
        - `cur` has all elements in `input` **once**.
        - Permutation I/II, Combination Sum II

    - Don't need `startIndex`, i.e., `startIndex` always equals to 0.
        - Letter Combination of a Phone Number

2. Condition to append `cur` to `results` (return_condition)

    - Always: e.g. Subsets
    - `len(cur) == len(input)`: e.g. Permutation
    - `startIndex == len(input)`: e.g. Palindrom Partitioning
    - Other conditions based on question requirements

3. Condition to avoid appending new element to `cur` (continue_condition)

    - Remove duplicate: Subsets II, Permutation II, etc.
    - Seen element: Permutation
    -  Other conditions based on question requirements

## 2. Binary Tree & Divide Conquer

<br/>

### 2.1 Selected Questions

<br/>

[94. Binary Tree Inorder Traversal](src/94.binary-tree-inorder-traversal.py)

[144. Binary Tree Preorder Traversal](src/144.binary-tree-preorder-traversal.py)

[145. Binary Tree Postorder Traversal *](src/145.binary-tree-postorder-traversal.py)

[257. Binary Tree Paths](src/257.binary-tree-paths.py)

[596. Minimum Subtree (Lintcode)](src/L596.minimum-subtree.py)

[110. Balanced Bianry Tree](src/110.balanced-binary-tree.py)

1120 Maximum Average Subtree $

[236. Lowest Common Ancestor of a Binary Tree](src/236.lowest-common-ancestor-of-a-binary-tree.py)

1644 Lowest Common Ancestor of a Binary Tree II $

1650 Lowest Common Ancestor of a Binary Tree III $

[98. Validate Binary Search Tree](src/98.validate-binary-search-tree.py)

426 Convert Binary Search Tree to Sorted Doubly Linked List $

[114. Flatten Binary Tree to Linked List](src/114.flatten-binary-tree-to-linked-list.py)

[173. Binary Search Tree Iterator](src/173.binary-search-tree-iterator.py)

285 Inorder Successor in BST $

[701. Insert into a Binary Search Tree](src/701.insert-into-a-binary-search-tree.py)

[100. Same Tree](src/100.same-tree.py)

[102. Binary Tree Level Order Traversal](src/102.binary-tree-level-order-traversal.py)

[814. Binary Tree Pruning](src/814.binary-tree-pruning.py)

[112. Path Sum](src/112.path-sum.py)

[129. Sum Root to Leaf Numbers](src/129.sum-root-to-leaf-numbers.py)

[508. Most Frequent Subtree Sum](src/508.most-frequent-subtree-sum.py)

[124. Binary Tree Maximum Path Sum *](src/124.binary-tree-maximum-path-sum.py)

[169. Majority Element *](src/169.majority-element.py)

[700. Search in a Binary Search Tree](src/700.search-in-a-binary-search-tree.py)

[1534. Convert Bineary Search Tree to Doubly Linked List (Lintcode)]

<br/>

### 2.2 Recursion in Binary Tree

<br/>

1. Tranverse vs Divide Conquer
   
   - Both are recursion algorithms.
   - Result in parameter vs result in return value
   - Top down vs bottom up
  
2. Four Elements of Recursion
    - 递归的定义：输入、输出、功能
    - 递归的拆解：大问题拆成小问题（例如二叉树，想想整棵树的结果和左右子树的结果之间是什么关系）
    - 递归的出口：何时返回（root is None，叶子结点）、返回值是什么
    - 递归的调用：各参数的初始值

<br/>

### 2.3 Time Complexity Analysis

<br/>
   
1. 通过`O(n)`的时间，把n的问题变成两个`n/2`的问题，复杂度是多少? `O(nlogn)`
   
   Example: merge sort, quick sort (average: `O(nlogn)`, worst: `O(n^2)`)
   
2. 通过`O(1)`的时间，把n的问题变成**两个**`n/2`的问题，复杂度是多少? `O(n)`

   Example: balanced binary tree

3. 通过`O(n)`的时间，把n的问题变成`n/2`的问题，复杂度是多少? `O(n)`
   
4. 通过`O(1)`的时间，把n的问题变成`n/2`的问题，复杂度是多少? `O(logn)`
   
   Example: [binary search](#3-binary-search)

5. Binary tree:
   
   Time: # of nodes x time for each node = `O(n)`
   
   Space: `O(h)`

6. 树形分析法复杂度

```
        n             O(n)
      /   \
    n/2   n/2         O(n/2) + O(n/2) = O(n)
    / \    / \
  n/4 n/4 n/4 n/4     O(n)
   ...     ...

height: O(logn), each level: O(n) ==> total time: O(nlogn)
```

```
         n
      /  |  \
    n/3 n/3 n/3     ==> O(nlogn)
    /|\  /|\ /|\
      ...  ...
```

```
        n             O(1)
      /   \
    n/2   n/2         O(2)
    / \    / \               ==> O(n)
  n/4 n/4 n/4 n/4     O(4)
   ...     ...
                      O(n)
```

## 3. Binary Search

<br/>

### 3.1 Selected Questions

<br/>

[278. First Bad Version](src/278.first-bad-version.py)

702 Search in a Sorted Array of Unknown Size $

[74. Search a 2D Matrix](src/74.search-a-2-d-matrix.py)

[34. Find First and Last Position of Element in Sorted Array](src/34.find-first-and-last-position-of-element-in-sorted-array.py)

[153. Find Minimum in Rotated Sorted Array](src/153.find-minimum-in-rotated-sorted-array.py)

[852. Peak Index in a Mountain Array](src/852.peak-index-in-a-mountain-array.py)

[162. Find Peak Element *](src/162.find-peak-element.py)

[33. Search in a Rotated Sorted Array](src/33.search-in-rotated-sorted-array.py)

[35. Search Insert Position](src/35.search-insert-position.py)

[69. Sqrt(x)](src/69.sqrt-x.py)

[240. Search a 2D Matrix II *](src/240.search-a-2-d-matrix-ii.py)

<br/>

### 3.2 Binary Search Template

<br/>

```python
def binarySearch(nums, target):
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    
    # find any/first position
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid
        else:
            right = mid

    if nums[left] == target:
        return left
    elif nums[right] == target:
        return right
    else:
        return -1

    # or to find any/last position
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid
        else:
            right = mid
    
    if nums[right] == target:
        return right
    elif nums[left] == target:
        return left
    else:
        return -1
```

Notes:

1. Condition to stop loop: `left + 1 < right`
   
   `left < right` might end up with dead loop:
   
   E.g.
   ```
   left = 2, right = 3, mid = 2
   left = mid = 2, right = 3, mid = 2
   ...
   ```

2. How to update left & right (when `nums[mid] == target`)?
   - Find any position: return
   - Find the first position: `right = mid`
   - Find the last position: `left = mid`

3. `mid = left + (right - left) // 2` vs `mid = (left + right) // 2`

   `left + right` might overflow if the values of `left` and `right` is very large.

4. Return value: `left` or `right`?
   - any position: any one `= target`
   - first position: `left` first if `nums[left] = target`
   - last position: `right` first if `nums[right] = target`

<br/>

## 4. BFS

### 4.1 Selected Questions

1. Serialize & Deserialize

   [449. Serialize and Deserialize BST](src/449.serialize-and-deserialize-bst.py)
   
   [297. Serialize and Deserialize Binary Tree](src/297.serialize-and-deserialize-binary-tree.py)
    
2. Traversal

   [107. Binary Tree Level Order Traversal II](src/107.binary-tree-level-order-traversal-ii.py)

   [429. N-ary Tree Level Order Traversal](src/429.n-ary-tree-level-order-traversal.py)

   [102. Binary Tree Level Order Traversal](src/102.binary-tree-level-order-traversal.py)

   [103. Binary Tree Zigzag Level Order Traversal](src/103.binary-tree-zigzag-level-order-traversal.py)

3. Graph

   [261.Graph Valid Tree (Lintcode 178)](src/L178.graph-valid-tree.py)

   [133. Clone Graph](src/133.clone-graph.py)

4. Topological Sorting
   
   [207. Course Scheduling *](src/207.course-schedule.py)
   
   [210. Course Scheduling II](src/210.course-schedule-ii.py)
   
   [444.Sequence Reconstruction (Lintcode 605)](src/L605.sequence-reconstruction.py)

5. Matrix  

   [200. Number of Islands *](src/200.number-of-islands.py)

   [598. Zombie in Matrix (Lintcode)](src/L598.zombie-in-matrix.py)

   [542. 01 Matrix](src/542.01-matrix.py)

   994 Rotting Oranges $

   1197 Minimum Knight Move $
   
   286 Walls and Gates $


### 4.2 BFS Template

```python
from collections import queue
def bfs(input):
    # 1. Initialize graph, indegree ...
    # 2. Get start nodes
    # 3. BFS
    queue = deque([startNodes])
    seen = {startNodes}  # optional
    while queue:
        qsize = len(queue)  # optional, only for level tranversal
        for _ in range(qsize):  # optional, only for level tranversal
            node = queue.popleft()
            for neighbor in all neighbors of node:
                if some_condition:  # optional
                    queue.append(neighbor)
                    seen.add(startNodes)
```

1. How to find neighbors?
   - Binary tree: `[node.left, node.right]`
   - Graph: `adjacent_list[node]`
   - Matrix: direction vector
      ```python
      dx = [-1, 0, 0, 1]
      dy = [0, -1, 1, 0]
      for i in range(4):
          x = x0 + dx[i]
          y = y0 + dy[i]
          ...
      ```

2. `seen` 
   - Binary tree: not necessary
   - Graph: hashset
   - Topological sorting: indegree
   - Matrix: mark original list

3. When to use BFS?
   - Graph traversal 
     - Connected area
     - Level traversal 
     - Topological Sorting
   - Shortest path in simple graph (unweighted and undirected)

<br/>

## 5. DFS

### 5.1 Selected Questions

[77. Combination](src/77.combinations.py)

```
784. Letter Case Permutation
314. Binary Tree Vertical Order Traversal
364. Nested List Weight Sum II
339. Nested List Weight Sum
698 Partition to K Equal Sum Subsets ***
51. N Queens
127. Word Ladder
126. Word Ladder II
```
