# Leetcode Notes

## Selected Questions 

1. Backtracking

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

    698. Partition to K Equal Sum Subsets (redo) memory optimization

    22. Generate Parentheses
    
    79. Word Search

    **DFS template:**
    
    ```python
    def helper(input, results, cur, startIndex):
        if return_condition:
            results.append(cur[:])
            return
        for i in range(startIndex, len(input)):
            if continue_condition:
                continue
            update startIndex
            update cur
            helper(input, results, cur, startIndex)
            recover cur # backtracking
    
    def main(input):
        results = []
        cur = []
        helper(input, results, cur, 0)
        return results
    ```
    
    Notes:
    
    1. How to update `startIndex`?
        
        Obejective: distinguish two adjacent recursion 
        
        - `cur` has all or part of elements in `input`. Each element appears **at most once**: `startIndex := i + 1`
            
            E.g. Subsets I/II, Palindrome Partitioning, Restore IP Address

        - `cur` has all or part of elements in `input`. Each element could appear **multiple times**: `startIndex := i`
            
            E.g. Combination Sum

        - `cur` has all elements in `input` **once**: `seen`
            
            E.g. Permutation I/II, Combination Sum II

        - Don't need `startIndex`, i.e., `startIndex` always equals to 0.
            
            E.g. Letter Combination of a Phone Number
    
    2. Condition to append `cur` to `results` (return_condition)

        - Always: e.g. Subsets
        - `len(cur) == len(input)`: e.g. Permutation
        - `startIndex == len(input)`: e.g. Palindrom Partitioning
        - Other conditions based on question requirements
    
    3. Condition to avoid appending new element to `cur` (continue_condition)

        - Remove duplicate: Subsets II, Permutation II, etc.
        - Seen element: Permutation
        -  Other conditions based on question requirements