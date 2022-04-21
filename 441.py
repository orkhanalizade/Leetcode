"""
441. Arranging Coins

You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Example 1:

Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        current = 1
        
        while n > 0:
            n -= current
            
            if n >= 0:
                rows += 1
                current += 1
                
        return rows

class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 0
        high = n

        while low <= high:
            mid = low + (high - low) // 2
            tillMid = mid * (mid + 1) // 2

            if tillMid == n:
                return mid
            elif tillMid < n:
                low = mid + 1
            else:
                high = mid - 1

        return high

Solution().arrangeCoins(5)