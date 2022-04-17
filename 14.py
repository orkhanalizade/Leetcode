"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        dict = {}
        searchRange = len(strs[0]) # 6

        if len(strs) == 1:
            return strs[0]

        # Fill dict with letters and indexes of the first word
        for i in range(0, len(strs[0])):
            dict[i] = strs[0][i]

        for i in range(1, len(strs)): # iterate through words in array
            word = strs[i]

            if len(word) < searchRange:
                searchRange = len(word)

            currentIndex = 0
            while currentIndex < searchRange:
                if word[currentIndex] == dict[currentIndex]:
                    currentIndex += 1

                    if currentIndex == searchRange:
                        currentIndex = 0
                        break
                else:
                    searchRange = currentIndex
                    continue

        print(strs[0][:searchRange])
        return strs[0][:searchRange]
            
Solution().longestCommonPrefix(["flower","flow","flight"])
# Solution().longestCommonPrefix(["dog","racecar","car"])