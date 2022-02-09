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
        cur = m + n
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            cur -= 1
            if nums1[m] >= nums2[n]:
                nums1[cur] = nums1[m]
                m -= 1
            else:
                nums1[cur] = nums2[n]
                n -= 1
        while m >= 0:
            cur -= 1
            nums1[cur] = nums1[m]
            m -= 1
        while n >= 0:
            cur -= 1
            nums1[cur] = nums2[n]
            n -= 1


  
            

        
# @lc code=end

