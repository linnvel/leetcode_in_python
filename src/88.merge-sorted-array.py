#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # idx = m + n - 1
        # m -= 1
        # n -= 1
        # while m >= 0 and n >= 0:
        #     if nums2[n] >= nums1[m]:
        #         nums1[idx] = nums2[n]
        #         n -= 1
        #     else:
        #         nums1[idx] = nums1[m]
        #         m -= 1
        #     idx -= 1
        # while m >= 0:
        #     nums1[idx] = nums1[m]
        #     idx -= 1
        #     m -= 1
        # while n >= 0:
        #     nums1[idx] = nums2[n]
        #     idx -= 1
        #     n -= 1          

        # Another implementation
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]
# @lc code=end

