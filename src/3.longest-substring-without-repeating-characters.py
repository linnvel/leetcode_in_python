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

        # Solution 1: dict
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

        # # Solution 2: queue
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

        # Solution 3: optimized dict (faster and cleaner)
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

