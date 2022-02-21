#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # # Solution 1: Sorting
        # # Time: O(nlogn), Space: O(1)/O(n)
        # nums.sort()
        # return nums[len(nums) // 2]

        # # Solution 2: Hash map
        # # Time: O(n), Space: O(n)
        # count = {}
        # for num in nums:
        #     if num in count:
        #         count[num] += 1
        #     else:
        #         count[num] = 1
        # for num, cnt in count.items():
        #     if cnt > len(nums) // 2:
        #         return num

        # # Solution 3: Divide and conquer
        # # Time: O(nlogn), Space: O(logn)
        # def findMajority(lo, hi):
        #     if lo == hi:
        #         return nums[lo]
        #     mid = (lo + hi) // 2
        #     left = findMajority(lo, mid)
        #     right = findMajority(mid + 1, hi)
        #     if left == right:
        #         return left
        #     cnt = 0
        #     for i in range(lo, hi + 1):
        #         cnt += 1 if nums[i] == left else -1
        #     return left if cnt > 0 else right
        # return findMajority(0, len(nums) - 1)

        # Solution 4: Boyer-Moore Voting Algorithm
        # Time: O(n), Space: O(1)
        candidate = None
        cnt = 0
        for num in nums:
            if cnt == 0:
                candidate = num
                cnt += 1
            else:
                cnt += 1 if num == candidate else -1
        return candidate

# @lc code=end

