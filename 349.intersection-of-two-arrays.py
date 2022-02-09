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
        # # solution 1: hashset
        # hashset = {}
        # interesect = set()
        # for num in nums1:
        #     if num not in hashset:
        #         hashset[num] = 1
        #     else:
        #         hashset[num] += 1
        
        # for num in nums2:
        #     if num in hashset:
        #         interesect.add(num)
        # return list(interesect)

        # # solution 2: binary search
        # def helper(short_arr, long_arr):
        #     short_arr.sort()
        #     interesect = set()
        #     for num in long_arr:
        #         l, r = 0, len(short_arr) - 1
        #         while l < r -1:
        #             mid = (l + r) // 2
        #             if short_arr[mid] <= num:
        #                 l = mid
        #             else:
        #                 r = mid
        #         if short_arr[l] == num or short_arr[r] == num:
        #             interesect.add(num)
        #     return list(interesect)

        # if len(nums1) < len(nums2):
        #     return helper(nums1, nums2)
        # else:
        #     return helper(nums2, nums1)

        # solution3: merge two sorted array
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        intersect = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                intersect.append(nums1[i])
                i += 1
                j += 1
                while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j] == nums1[i-1]:
                    i += 1
                    j += 1
        return intersect


        
# @lc code=end

