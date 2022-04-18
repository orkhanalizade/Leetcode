"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for letter in s:
            if letter in dict:
                if len(stack) > 0 and stack[-1] == dict[letter]:
                    stack.pop()
                else:
                    stack.append(letter)
            else:
                stack.append(letter)

        print(len(stack) == 0)
        return len(stack) == 0

# Solution().isValid("()[]{}")
# Solution().isValid("()")
# Solution().isValid("(]")
Solution().isValid("]")