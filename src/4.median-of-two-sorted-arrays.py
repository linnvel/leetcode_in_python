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
        # l1, r1 = 0, len(nums1) - 1
        # l2, r2 = 0, len(nums2) - 1
        # while l1 <= r1 and l2 <= r2:
        #     mid1 = (l1 + r1) // 2
        #     mid2 = (l2 + r2) // 2
        #     if nums1[mid1] == nums2[mid2]:
        #         return nums1[mid1]
        #     elif nums1[mid1] < nums2[mid2]:
        #         l1 = mid1
        #         r2 = mid2
        #     else:
        #         r1 = mid1
        #         l2 = mid2
        # if l1 <= r1:
        #     if (r1 - l1) % 2 == 0:
        #         return nums1[(l1 + r1) // 2]
        #     else:
        #         return (nums1[(l1 + r1) // 2] + nums1[(l1 + r1) // 2 + 1]) / 2
        # elif l2 <= r2:
        #     if (r2 - l2) % 2 == 0:
        #         return nums2[(l2 + r2) // 2]
        #     else:
        #         return (nums2[(l2 + r2) // 2] + nums2[(l2 + r2) // 2 + 1]) / 2

        # Solution 1: merge --> return nums[(m + n) // 2]
        # Time complexity: O(m + n)

        # Solution 2: find kth largest --> return findkth((m + n) // 2)
        # Binary search: k --> k/2 --> k/4 ...
        # Time complexith: O(logk)
        def findKth(nums1, nums2, k):
            if len(nums1) == 0:
                return nums2[k - 1]
            if len(nums2) == 0:
                return nums1[k - 1]
            if k == 1:
                return min(nums1[0], nums2[0])
            index1 = min(len(nums1) - 1, k // 2 - 1)
            index2 = min(len(nums2) - 1, k // 2 - 1)
            if nums1[index1] < nums2[index2]:
                return findKth(nums1[index1 + 1:], nums2, k - index1 - 1)
            else:
                return findKth(nums1, nums2[index2 + 1:], k - index2 - 1)
        
        m, n = len(nums1), len(nums2)
        if (m + n) % 2 == 0:
            median1 = findKth(nums1, nums2, (m + n) // 2 +1)
            median2 = findKth(nums1, nums2, (m + n) // 2)
            return (median1 + median2) / 2.0
        else:
            return findKth(nums1, nums2, (m + n) // 2 + 1)

# @lc code=end

