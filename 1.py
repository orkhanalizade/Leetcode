"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i in range(0, len(nums)):
            key = target - nums[i]

            if key in dict:
                print([dict[key], i])
                return [dict[key], i]
            else:
                dict[nums[i]] = i

        return []

Solution().twoSum([2,7,11,15], 9)
Solution().twoSum([3,2,4], 6)
Solution().twoSum([3,3], 6)