"""
9. Palindrome Number

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)

        for i in range(0, len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False

        return True

Solution().isPalindrome(123212)