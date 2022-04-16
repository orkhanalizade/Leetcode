"""
852. Peak Index in a Mountain Array

Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

 

Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1
"""

from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                print(mid)
                return mid

            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1

        print(mid)
        return mid

# Solution().peakIndexInMountainArray([0, 10, 5, 2])
# Solution().peakIndexInMountainArray([0, 2, 1, 0])
Solution().peakIndexInMountainArray([0, 1, 0])