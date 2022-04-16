#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import heapq
        d = {}
        for word in words:
            if word in d:
                d[word] -= 1
            else:
                d[word] = -1

        # Solution 1: heap
        #  hq = []
        # heapq.heapify(hq)
        # for word, cnt in d.items():
        #     heapq.heappush(hq, (cnt, word))
        # results = heapq.nsmallest(k, hq)
        # return [res[1] for res in results]

        # Solution 2: sort (faster)
        res = sorted(d, key = lambda x: (d[x], x))
        return res[:k]
# @lc code=end

