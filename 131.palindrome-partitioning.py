#
# @lc app=leetcode id=131 lang=python
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def getIsPalindrome(s):
            isPalindrome = [[False] * len(s) for _ in range(len(s))]
            for i in range(len(s)):
                isPalindrome[i][i] = True
            for i in range(len(s) - 1):
                isPalindrome[i][i + 1] = (s[i] == s[i + 1])
            for j in range(1, len(s) // 2 + 1):
                for i in range(len(s) - 2 * j):
                    isPalindrome[i][i + 2 * j] = isPalindrome[i + 1][i + 2 * j - 1] and (s[i] == s[i + 2 * j])
                    if i + 2 * j < len(s) - 1:
                        isPalindrome[i][i + 2 * j + 1] = isPalindrome[i + 1][i + 2 * j] and (s[i] == s[i + 2 * j + 1])
            return isPalindrome

        isPalindrome = getIsPalindrome(s)

        def helper(s, startIndex, partition, results, isPalindrome):
            if startIndex == len(s):
                results.append(partition[:])  # hard copy
            for i in range(startIndex, len(s)):
                if not isPalindrome[startIndex][i]:
                    continue
                sub = s[startIndex : i + 1]
                partition.append(sub)
                helper(s, i + 1, partition, results, isPalindrome)
                partition.pop()
 
        results = []
        partition = []
        helper(s, 0, partition, results, isPalindrome)
        return results


                

        
# @lc code=end

