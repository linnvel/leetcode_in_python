# Leetcode Top Interview Questions

Problems list:<br>
https://leetcode.com/problem-list/top-interview-questions/?sorting=W3t9XQ%3D%3D

Time records:<br>
https://leetplug.azurewebsites.net/data?userId=1704

<table border="1">
  <thead>
    <tr>
      <th rowspan="2">Problem</th>
      <th rowspan="2">Link</th>
      <th rowspan="2">Difficulty</th>
      <th rowspan="2">Solution</th>
      <th colspan="2">Complexity</th>
      <th rowspan="2">Notes</th>
      <th colspan="2">Time</th>
    </tr>
    <tr>
      <th>Time</th>
      <th>Space</th>
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
      <td>Solution 2: find kth largest + binary search</td>
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
      <td>Solution 2: DP</td>
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