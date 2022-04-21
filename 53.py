"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = nums[0]
        currSum = 0

        for n in nums:
            currSum += n

            answer = max(answer, currSum)
            currSum = max(currSum, 0)

        return answer

Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
