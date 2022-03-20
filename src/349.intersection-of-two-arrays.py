#
# @lc app=leetcode id=349 lang=python
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Solution 1: Hash set
        nums = set(nums1)
        results = set()
        for num in nums2:
            if num in nums:
                results.add(num)
        return list(results)

        # Solution 2: binary search
        # Solution 3: merge two sorted array


        
# @lc code=end

