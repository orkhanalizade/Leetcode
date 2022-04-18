"""
744. Find Smallest Letter Greater Than Target

Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
 

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Example 3:

Input: letters = ["c","f","j"], target = "d"
Output: "f"
"""

from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        dict = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,

            "f": 6,
            "g": 7,
            "h": 8,
            "i": 9,
            "j": 10,

            "k": 11,
            "l": 12,
            "m": 13,
            "n": 14,
            "o": 15,

            "p": 16,
            "q": 17,
            "r": 18,
            "s": 19,
            "t": 20,

            "u": 21,
            "v": 22,
            "w": 23,
            "x": 24,
            "y": 25,
            "z": 26            
        }

        low = 0
        high = len(letters) - 1
        answer = letters[0]

        while low <= high:
            mid = low + (high - low) // 2

            if dict[letters[mid]] > dict[target]:
                high = mid - 1
                answer = letters[mid]
            else:
                low = mid + 1

        return answer

Solution().nextGreatestLetter(["c","f","j"], "a")
Solution().nextGreatestLetter(["c","f","j"], "c")
Solution().nextGreatestLetter(["c","f","j"], "d")
Solution().nextGreatestLetter(["c","f","j"], "j")

