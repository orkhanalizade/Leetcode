from itertools import count

"""
Time complexity:  O(n)
Space complexity: O(1)
"""
class Solution:
    def maxDepth(self, s: str) -> int:
        result = count = 0

        for letter in s:
            if letter == "(":
                count += 1
                result = max(result, count)
            elif letter == ")":
                count -= 1
        
        return result


"""
Time complexity:  O(n)
Space complexity: O(n)
"""
class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        result = 0

        for letter in s:
            if letter == "(":
                stack.append("(")
                result = max(result, len(stack))
            elif letter == ")":
                stack.pop()

        return result


Solution().maxDepth("(1+(2*3)+((8)/4))+1")

