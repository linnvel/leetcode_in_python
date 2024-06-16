#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

from collections import Counter
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # # Solution 1: sliding window
        # # time: 2|s| + |t|
        # # space: |s| + |t|
        # c = Counter(t)
        # required = len(c)
        # formed = 0
        # window_counter = Counter()
        # l, r = 0, 0
        # result = s + 'a'
        # while r < len(s):
        #     character = s[r]
        #     if character in c:
        #         window_counter.update(character)
        #         if c[character] == window_counter[character]:
        #             formed += 1
        #         while l <= r and formed == required:
        #             if len(result) > r - l + 1:
        #                 result = s[l : r + 1]
        #             character = s[l]
        #             if character in c:
        #                 window_counter[character] -= 1
        #                 if window_counter[character] < c[character]:
        #                     formed -= 1
        #             l += 1
        #     r += 1
        # return result if len(result) <= len(s) else ""

        # Solution 2: optimized sliding window
        # time: 2|filtered_s| + |s| + |t|
        # space: |filtered_s| + |s| + |t|
        # efficient when |t| << |s|
        c = Counter(t)
        filtered_s = []
        for i in range(len(s)):
            if s[i] in c:
                filtered_s.append((i, s[i]))

        required = len(c)
        formed = 0
        window_counter = Counter()
        l, r = 0, 0
        result = s + 'a'
        while r < len(filtered_s):
            ir, character = filtered_s[r]
            if character in c:
                window_counter.update(character)
                if c[character] == window_counter[character]:
                    formed += 1
                while formed == required and l <= r:
                    il, character = filtered_s[l]
                    if len(result) > ir - il + 1:
                        result = s[il : ir + 1]
                    if character in c:
                        window_counter[character] -= 1
                        if window_counter[character] < c[character]:
                            formed -= 1
                    l += 1
            r += 1
        return result if len(result) <= len(s) else ""


# @lc code=end

