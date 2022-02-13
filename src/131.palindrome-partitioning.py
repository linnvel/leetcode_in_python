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

        # preprocessing
        def getPalindrome(s):
            n = len(s)
            palindrome = [[None for _ in range(n)] for _ in range(n)]
            for i in range(n):
                palindrome[i][i] = True
                if i < n - 1:
                    palindrome[i][i + 1] = s[i] == s[i + 1]
            # i -> j is not correct
            # for i in range(n - 1):
            #     for j in range(i + 2, n):

            # j -> i is correct
            for j in range(2, n):
                for i in range(j - 1):
                    palindrome[i][j] = palindrome[i + 1][ j - 1] and s[i] == s[j]
            return palindrome

        def helper(s, startIndex, cur, results, palindrome):
            if startIndex == len(s):
                results.append(cur[:])
            for i in range(startIndex, len(s)):
                if not palindrome[startIndex][i]:
                    continue
                cur.append(s[startIndex : i + 1])
                helper(s, i + 1, cur, results, palindrome)
                cur.pop()

        palindromeMatrix = getPalindrome(s)
        results = []
        cur = []
        helper(s, 0, cur, results, palindromeMatrix)
        return results   

        
# @lc code=end

