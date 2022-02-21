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
