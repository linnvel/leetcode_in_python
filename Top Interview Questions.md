# Leetcode Top Interview Questions

Problem list:<br>
https://leetcode.com/problem-list/top-interview-questions/?sorting=W3t9XQ%3D%3D

Time records:<br>
https://leetplug.azurewebsites.net/data?userId=1704

Error list:<br>
https://leetcode.com/list/

<table>
  <thead>
    <tr>
      <th rowspan="2">Problem</th>
      <th rowspan="2">Link</th>
      <th rowspan="2">Difficulty</th>
      <th rowspan="2">Solution</th>
      <th rowspan="2">Time Complexity</th>
      <th rowspan="2">Space Complexity</th>
      <th rowspan="2">Notes</th>
      <th colspan="2">Time</th>
    </tr>
    <tr>
      <th>1st</th>
      <th>2nd</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1. Two Sum</td>
      <td><a href=https://leetcode.com/problems/two-sum/submissions>leetcode</a>
      <td>Easy</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/1.two-sum.py>Solution</a></td>
      <td>O(n)</td>
      <td>O(n)</td>
      <td>Unique array: hashset<br>Sorted array: two pointers</td>
      <td>1'42"</td>
      <td></td>
    </tr>
    <tr>
      <td>2. Add Two Numbers</td>
      <td><a href=https://leetcode.com/problems/add-two-numbers>leetcode</a>
      <td>Medium</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/2.add-two-numbers.py>Solution</a></td>
      <td>O(n)</td>
      <td>O(n)</td>
      <td>Follow up: Update list in-place to use less memory</td>
      <td>5'48"</td>
      <td>7'06"</td>
    </tr>
    <tr>
      <td>3. Longest Substring Without Repeating Characters</td>
      <td><a href=https://leetcode.com/problems/longest-substring-without-repeating-characters>leetcode</a>
      <td>Medium</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/3.longest-substring-without-repeating-characters.py>Solution</a></td>
      <td>O(n)</td>
      <td>O(min(m, n))</td>
      <td>Sliding window with hashset:<br>1) {character: count}: 2n steps<br>2) {character:index}: n steps by optimization</td>
      <td>17'11"</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">4. Median of Two Sorted Arrays</td>
      <td rowspan="2"><a href=https://leetcode.com/problems/median-of-two-sorted-arrays>leetcode</a>
      <td rowspan="2">Hard</td>
      <td rowspan="2"><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/4.median-of-two-sorted-arrays.py>Solution</a></td>
      <td>O(n)</td>
      <td>O(n)</td>
      <td>Solution 1: merge two sorted array</td>
      <td>10'20"</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Solution 2: find kth largest + binary search (Todo)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>7. Reverse Integer</td>
      <td><a href=https://leetcode.com/problems/reverse-integer>leetcode</a>
      <td>Medium</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/7.reverse-integer.py>Solution</a></td>
      <td>O(lg(x))</td>
      <td>O(1)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>8. String to Integer (atoi)</td>
      <td><a href=https://leetcode.com/problems/string-to-integer-atoi>leetcode</a>
      <td>Medium</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/8.string-to-integer-atoi.py>Solution</a></td>
      <td>O(n)</td>
      <td>O(1)</td>
      <td>Overflow condition: ans > MAX_INT // 10 or (ans == MAX_INT // 10 and d > 7)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">10. Regular Expression Matching</td>
      <td rowspan="2"><a href=https://leetcode.com/problems/median-of-two-sorted-arrays>leetcode</a>
      <td rowspan="2">Hard</td>
      <td rowspan="2"><a href="https://github.com/linnvel/leetcode_in_python/blob/master/src/10.regular-expression-matching.py">Solution</a></td>
      <td>O((T+P)*2^(T+P/2))</td>
      <td>O((T+P)*2^(T+P/2))</td>
      <td>Solution 1: recursion (DFS), <a href=https://levelup.gitconnected.com/solving-for-recursive-complexity-736439987cb0>complexity analysis</a></td>
      <td>23h36'33"</td>
      <td></td>
    </tr>
    <tr>
      <td>O(T*P)</td>
      <td>O(T*P)</td>
      <td>Solution 2: DFS with memorization</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11. Container With Most Water</td>
      <td><a href=https://leetcode.com/problems/container-with-most-water>leetcode</a>
      <td>Medium</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/11.container-with-most-water.py>Solution</a></td>
      <td>O(n)</td>
      <td>O(1)</td>
      <td><a href=https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation/880632>Greedy explanation</a>: let say (0, 8) height[0] is less than height[8], so no need to check for (0, 1) ... (0, 7) because width = j-i is going to decrease and height = min(height[i], height[j]) will either remain constant or decrease.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13. Roman to Integer</td>
      <td><a href=https://leetcode.com/problems/roman-to-integer>leetcode</a>
      <td>Easy</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/13.roman-to-integer.py>Solution</a></td>
      <td>O(n)</td>
      <td>O(1)</td>
      <td></td>
      <td>9'33"</td>
      <td></td>
    </tr>
    <tr>
      <td>14. Longest Common Prefix</td>
      <td><a href=https://leetcode.com/problems/longest-common-prefix>leetcode</a>
      <td>Easy</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/14.longest-common-prefix.py>Solution</a></td>
      <td>O(S)</td>
      <td>O(1)</td>
      <td></td>
      <td>7'11"</td>
      <td></td>
    </tr>   
    <tr>
      <td>17. Letter Combinations of a Phone Number</td>
      <td><a href=https://leetcode.com/problems/letter-combinations-of-a-phone-number>leetcode</a>
      <td>Medium</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/17.letter-combinations-of-a-phone-number.py>Solution</a></td>
      <td>O(4^n)</td>
      <td>O(4^n)</td>
      <td>DFS</td>
      <td>34'19"</td>
      <td></td>
    </tr>
    <tr>
      <td>19. Remove Nth Node From End of List</td>
      <td><a href=https://leetcode.com/problems/remove-nth-node-from-end-of-list>leetcode</a>
      <td>Medium</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/19.remove-nth-node-from-end-of-list.py>Solution</a></td>
      <td>O(n)</td>
      <td>O(1)</td>
      <td>One path solution - fast/slow pointers: n steps ahead</td>
      <td>30'</td>
      <td></td>
    </tr>
    <tr>
      <td>20. Valid Parentheses</td>
      <td><a href=https://leetcode.com/problems/valid-parentheses>leetcode</a>
      <td>Easy</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/20.valid-parentheses.py>Solution</a></td>
      <td>O(n)</td>
      <td>O(n)</td>
      <td>Stack</td>
      <td>3'47"</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">21. Merge Two Sorted Lists</td>
      <td rowspan="2"><a href=https://leetcode.com/problems/merge-two-sorted-lists>leetcode</a>
      <td rowspan="2">Easy</td>
      <td rowspan="2"><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/21.merge-two-sorted-lists.py>Solution</a></td>
      <td rowspan="2">O(n)</td>
      <td rowspan="2">O(1)</td>
      <td>Solution 1: dummy node</td>
      <td>13'33"</td>
      <td></td>
    </tr>
    <tr>
    <td>Solution 2: without dummy node</td>
    <td></td>
    <td></td>
    </tr>
    <tr>
      <td>22. Generate Parentheses</td>
      <td><a href=https://leetcode.com/problems/generate-parentheses>leetcode</a>
      <td>Medium</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/22.generate-parentheses.py>Solution</a></td>
      <td>O(4^n/sqrt(n))</td>
      <td>O(4^n/sqrt(n))</td>
      <td>DFS</td>
      <td>4'1"</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="3">23. Merge k Sorted Lists</td>
      <td rowspan="3"><a href=https://leetcode.com/problems/merge-k-sorted-lists>leetcode</a>
      <td rowspan="3">Hard</td>
      <td rowspan="3"><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/23.merge-k-sorted-lists.py>Solution</a></td>
      <td>O(Nlogk)</td>
      <td>O(Nlogk)</td>
      <td>Solution 1: Divide and conquer (top down recursion)</td>
      <td>10'12"</td>
      <td></td>
    </tr>
    <tr>
      <td>O(Nlogk)</td>
      <td>O(1)</td>
      <td>Solution 2: Merge sort (Bottom up iteration)</a></td>
      <td>10'4"</td>
      <td></td>
    </tr>   
    <tr>
      <td>O()</td>
      <td>O()</td>
      <td>Solution 3: Priority queue (todo)</a></td>
      <td></td>
      <td></td>
    </tr>   
    <tr>
      <td>26. Remove Duplicates from Sorted Array</td>
      <td><a href=https://leetcode.com/problems/remove-duplicates-from-sorted-array>leetcode</a>
      <td>Easy</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/26.remove-duplicates-from-sorted-array.py>Solution</a></td>
      <td>O(n)</td>
      <td>O(1)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">28. Find the Index of the First Occurrence in a String</td>
      <td rowspan="2"><a href=https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string>leetcode</a>
      <td rowspan="2">Medium</td>
      <td rowspan="2"><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/28.find-the-index-of-the-first-occurrence-in-a-string.py>Solution</a></td>
      <td>O(mn)</td>
      <td>O(1)</td>
      <td>Solution 1: brute force</td>
      <td>8'20"</td>
      <td></td>
    </tr>
    <tr>
      <td>O(n+m)</td>
      <td>O(n)</td>
      <td><a href=https://www.youtube.com/watch?v=GTJr8OvyEVQ>Solution 2: KMP pattern match</a></td>
      <td></td>
      <td></td>
    </tr>    
    <tr>
      <td>29. Divide Two Integers</td>
      <td><a href=https://leetcode.com/problems/divide-two-integers>leetcode</a>
      <td>Medium</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/29.divide-two-integers.py>Solution</a></td>
      <td>???</td>
      <td>O(1)</td>
      <td>E.g. 58 = 2^3*5 + 2^0*5 + 3 = (2^3 + 2^0) * 5 + 3 => quotient = 2^3 + 2^0</td>
      <td>>24h</td>
      <td></td>
    </tr>
    <tr>
      <td>33. Search in Rotated Sorted Array</td>
      <td><a href=https://leetcode.com/problems/search-in-rotated-sorted-array>leetcode</a>
      <td>Medium</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/33.search-in-rotated-sorted-array.py>Solution</a></td>
      <td>O(logn)</td>
      <td>O(1)</td>
      <td></td>
      <td>20'4"</td>
      <td></td>
    </tr>
    <tr>
      <td>34. Find First and Last Position of Element in Sorted Array</td>
      <td><a href=https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array>leetcode</a>
      <td>Medium</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/34.find-first-and-last-position-of-element-in-sorted-array.py>Solution</a></td>
      <td>O(logn)</td>
      <td>O(1)</td>
      <td>Binary search</td>
      <td>13'40"</td>
      <td></td>
    </tr>
    <tr>
      <td>36. Valid Sudoku</td>
      <td><a href=https://leetcode.com/problems/valid-sudoku>leetcode</a>
      <td>Medium</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/36.valid-sudoku.py>Solution</a></td>
      <td>O(n^2)</td>
      <td>O(n^2)</td>
      <td></td>
      <td>27'41"</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="3">42. Trapping Rain Water</td>
      <td rowspan="3"><a href=https://leetcode.com/problems/trapping-rain-water>leetcode</a>
      <td rowspan="3">Hard</td>
      <td rowspan="3"><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/42.trapping-rain-water.py>Solution</a></td>
      <td>O(n^2)</td>
      <td>O(1)</td>
      <td>Solution 1: Brute force (TLE)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>O(n)</td>
      <td>O(n)</td>
      <td>Solution 2: DP</a></td>
      <td>1h8'32"</td>
      <td></td>
    </tr>  
    <tr>
      <td>O(n)</td>
      <td>O(1)</td>
      <td>Solution 3: DP space optimization</a></td>
      <td></td>
      <td></td>
    </tr>  
    <tr>
      <td rowspan="3">44. Wildcard Matching</td>
      <td rowspan="3"><a href=https://leetcode.com/problems/wildcard-matching>leetcode</a>
      <td rowspan="3">Hard</td>
      <td rowspan="3"><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/44.wildcard-matching.py>Solution</a></td>
      <td>O()</td>
      <td>O()</td>
      <td>Solution 1: DFS (TLE)</td>
      <td></td>
      <td></td>
    </tr>   
    <tr>
      <td>O(m*n)</td>
      <td>O(m*n)</td>
      <td>Solution 2: DFS with memorization (@lru_cache decorator)</a></td>
      <td>52'38"</td>
      <td></td>
    </tr>  
    <tr>
      <td>O(m*n)</td>
      <td>O(m*n)</td>
      <td>Solution 3: 2d DP</a></td>
      <td></td>
      <td></td>
    </tr>   
    <tr>
      <td>46. Permutations</td>
      <td><a href=https://leetcode.com/problems/permutations>leetcode</a>
      <td>Medium</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/46.permutations.py>Solution</a></td>
      <td>O(2^n)</td>
      <td>O(2^n)</td>
      <td>Backtracking + seen</td>
      <td>7'32"</td>
      <td></td>
    </tr>
    <tr>
      <td>48. Rotate Image</td>
      <td><a href=https://leetcode.com/problems/rotate-image>leetcode</a>
      <td>Medium</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/src/48.rotate-image.py>Solution</a></td>
      <td>O(n^2)</td>
      <td>O(1)</td>
      <td>Solution 1: rotate groups of four cells; <br>
      Solution 2: reverse diagonal + reverse left to right (i.e. transpose + reflect)</td>
      <td>23'50"</td>
      <td></td>
    </tr>    
    <tr>
      <td></td>
      <td><a href=>leetcode</a>
      <td>Medium</td>
      <td><a href=https://github.com/linnvel/leetcode_in_python/blob/master/>Solution</a></td>
      <td>O()</td>
      <td>O()</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>  