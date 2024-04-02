# Wrong Question Set

* [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/?envType=study-plan-v2&envId=top-interview-150)
  
  Trick: append current result in the opposite order

* [124.Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/?envType=study-plan-v2&envId=top-interview-150)
  
  Tricks: smart post tranverse recursion
  1) updating current price with left + root + right, where left = max(left, 0), right = max(right, 0) 
  2) updating global/nonlocal maximum variable with max(current, maximum)
  3) return the larger sum of branch, i.e. root + max(left, right) 
  
  In short, recursion can only record one branch. Paths with two branches are recorded by the global maximum variable. 

  A good explanation: https://leetcode.com/problems/binary-tree-maximum-path-sum/solutions/603423/python-recursion-stack-thinking-process-diagram/?envType=study-plan-v2&envId=top-interview-150

* [200.Number of Islands](https://leetcode.com/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150)
  
  Tricks: 
  1) flood filling - mark seen node to 0 (empty value) 
  2) coordinate transformation of matrix:
    ```
    dx = [0, 1, 0, -1]  # don't forget to look back
    dy = [1, 0, -1, 0]
    for i in range(len(dx)):
        x += dx[i]
        y += dy[i]
    ```

    Todo: union find