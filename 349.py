"""
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.


Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = {}
        list = []

        for n1 in nums1:
            hashMap[n1] = 1

        for n2 in nums2:
            if n2 in hashMap:
                list.append(n2)
                del hashMap[n2]

        print(list)

        return list

Solution().intersection([1,2,2,1], [2,2])
