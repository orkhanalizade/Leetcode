"""
367. Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        low = 0
        high = num // 2

        while low <= high:
            mid = low + (high - low) // 2

            if mid * mid == num:
                return True

            if mid * mid > num:
                high = mid - 1
            else:
                low = mid + 1

        return False

Solution().isPerfectSquare(1)