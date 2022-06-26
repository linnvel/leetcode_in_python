#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Solution 1: DP
        # steps = {stone: set() for stone in stones}
        # steps[stones[0]].add(1)
        # for stone in stones[:-1]:
        #     step = steps[stone]
        #     for k in step:
        #         if stone + k in steps:
        #             for n in [k - 1, k , k + 1]:
        #                 if n > 0 and n not in steps[stone + k]:
        #                     steps[stone + k].add(n)
        # return len(steps[stones[-1]]) > 0

        # Solution 2: DFS(TLE)
        # def dfs(stones, curStone, prev, target):
        #     if curStone == target:
        #         return True
        #     for k in [prev - 1, prev, prev + 1]:
        #         if k >= 1 and curStone + k in stones and dfs(stones, curStone + k, k, target):
        #             return True
        #     return False
        # return dfs(set(stones), stones[0], 0, stones[-1])


        # Solution 3: DFS with memorization
        global steps
        steps = {}
        steps[(stones[0], 0)] = True
        def dfs(stones, curStone, prev, target):
            if curStone == target:
                return True
            for k in [prev - 1, prev, prev + 1]:
                if k >= 1 and curStone + k in stones:
                    if (curStone + k, k) not in steps:
                        steps[(curStone + k, k)] = dfs(stones, curStone + k, k, target)
                    if steps[(curStone + k, k)]:
                        return True
            return False
        
        return dfs(set(stones), stones[0], 0, stones[-1])

# @lc code=end

