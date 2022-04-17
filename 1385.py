"""
1385. Find the Distance Value Between Two Arrays

Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation: 
For arr1[0]=4 we have: 
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
For arr1[1]=5 we have: 
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
"""

from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0

        for n in arr1:
            low = 0
            high = len(arr2) - 1

            while low <= high:
                mid = low + (high - low) // 2

                if abs(n - arr2[mid]) <= d:
                    count -= 1
                    break

                if arr2[mid] > n:
                    high = mid - 1
                else:
                    low = mid + 1

            count += 1

        return count

Solution().findTheDistanceValue([4,5,8], [10,9,1,8], 2)
Solution().findTheDistanceValue([1,4,2,3], [-4,-3,6,10,20,30], 3)
Solution().findTheDistanceValue([2,1,100,3], [-5,-2,10,-3,7], 6)
Solution().findTheDistanceValue([-3,10,2,8,0,10], [-9,-1,-4,-9,-8, 2], 9)