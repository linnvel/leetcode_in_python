#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        """
        Solution 1: Sliding window with hashset
        Time complexity : O(2n) = O(n). In the worst case each character will be visited twice by l and r.
        Space complexity : O(min(m,n)). We need O(k) space for the sliding window, where k is the size of the Set. 
        The size of the Set is upper bounded by the size of the string n and the size of the charset/alphabet m.
        """
        # h = {s[0]: 0}
        # l, r = 0, 1
        # maxlen = 1
        # while r < len(s):
        #     if s[r] in h:
        #         start = h[s[r]]
        #         for i in range(l, start + 1):  # this loop is not necessary, can be optimized
        #             del h[s[i]]
        #         maxlen = max(maxlen, r - l)
        #         l = start + 1
        #     h[s[r]] = r
        #     r += 1
        # maxlen = max(maxlen, r - l)
        # return maxlen

        """
        Solution 2: Sliding window with queue
        """
        # from collections import deque
        # q = deque()
        # maxLen = 0
        # for element in s:
        #     if element in q:
        #         maxLen = max(maxLen, len(q))
        #         cur = q.popleft()
        #         while cur != element:
        #             cur = q.popleft()
        #     q.append(element)
        # return max(maxLen, len(q))

        """
        Solution 3: Optimized Sliding window with hashset (faster and cleaner)
        Time complexity : O(n). Index r will iterate n times.
        Space complexity : O(min(m, n)). Same as the previous approach.
        """
        h = {}
        l, r = 0, 0
        maxlen = 1
        while r < len(s):
            if s[r] in h:
                l = max(l, h[s[r]] + 1)
            h[s[r]] = r
            r += 1
            maxlen = max(maxlen, r - l)
        return maxlen

        
# @lc code=end

