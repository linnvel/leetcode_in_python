# Leetcode Notes

- [Leetcode Notes](#leetcode-notes)
  - [1. Backtracking](#1-backtracking)
    - [Selected Questions](#selected-questions)
    - [Summary: Backtracking template](#summary-backtracking-template)
  - [2. Binary Tree & Divide Conquer](#2-binary-tree--divide-conquer)
    - [Selected Questions](#selected-questions-1)

---

## 1. Backtracking

### Selected Questions

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

### Summary: Backtracking template
    
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

### Selected Questions

[94. Binary Tree Inorder Traversal](src/94.binary-tree-inorder-traversal.py)
[144. Binary Tree Preorder Traversal](src/144.binary-tree-preorder-traversal.py)

```
1.   Binary Tree Postorder Traversal
2.   Binary Tree Paths
3. Minimum Subtree
4.   Balanced Bianry Tree
5.    Maximum Average Subtree
6.   Lowest Common Ancestor of a Binary Tree
7.    Lowest Common Ancestor of a Binary Tree II
8.    Lowest Common Ancestor of a Binary Tree III
9.  Validate Binary Search Tree
10.  Convert Binary Search Tree to Sorted Doubly Linked List
11.  Flatten Binary Tree to Linked List
12.  Binary Search Tree Iterator
13.  Inorder Successor in BST
14.  Insert into a Binary Search Tree
15.  Same Tree
16.  Binary Tree Level Order Traversal
814, Binary Tree Pruning
1.   Path Sum
2.   Sum Root to Leaf Numbers
3.   Most Frequent Subtree Sum
4.   Binary Tree Maximum Path Sum
5.   Majority Element
6.   Search in a Binary Search Tree
7.   Inorder Successor in BST
```