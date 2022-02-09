#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if (m + n) % 2 != 0:
            k = (m + n) // 2 + 1
            return self.findkth(nums1, nums2, k)
        else:
            k = (m + n) // 2
            val1 = self.findkth(nums1, nums2, k)
            val2 = self.findkth(nums1, nums2, k + 1)
            # print(val1, val2, k)
            return (val1 + val2) * 1.0 / 2


    # def findkandkplus(self, nums1, nums2, k):
    #     if len(nums1) == 0:
    #         return nums2[k - 1], nums2[k] if k >= 1 else None, nums2[k]
    #     if len(nums2) == 0:
    #         return nums1[k - 1], nums1[k] if k >= 1 else None, nums1[k]
    #     if k == 0:
    #         return None, min(nums1[0], nums2[0])
    #     if k == 1:
    #         if nums1[0] <= nums2[0]:
    #             return nums1[0], min(nums1[1], nums2[0])
    #         else:
    #             return nums2[0], min(nums1[0], nums2[1])
    #     if nums1[k // 2 - 1] <= nums2[k // 2 - 1]:
    #         return self.findkandkplus(nums1[k // 2:], nums2, k - k//2)
    #     else:
    #         return self.findkandkplus(nums1, nums2[k//2:], k - k//2)

    def findkth(self, nums1, nums2, k):
        if len(nums1) == 0:
            return nums2[k - 1]
        if len(nums2) == 0:
            return nums1[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        
        index1 = min(k // 2 - 1, len(nums1) - 1)
        index2 = min(k // 2 - 1, len(nums2) - 1)
        if nums1[index1] <= nums2[index2]:
            return self.findkth(nums1[index1 + 1:], nums2, k - (index1 + 1))
        else:
            return self.findkth(nums1, nums2[index2 + 1:], k - (index2 + 1))


# @lc code=end

