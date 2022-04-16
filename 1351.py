"""
1351. Count Negative Numbers in a Sorted Matrix

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
 

Follow up: Could you find an O(n + m) solution?
"""

from itertools import count
from typing import List

from pyparsing import col

"""
Time Complexity:  O(mlogn)
Space Complexity: O(1)
"""
# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#         count = 0

#         for i in range(0, len(grid)):
#             low = 0
#             high = len(grid[i]) - 1

#             while low <= high:
#                 mid = (low + high) // 2

#                 if grid[i][mid] >= 0:
#                     low = mid + 1
#                 else:
#                     high = mid - 1

#             count += (len(grid[i]) - high - 1)

#         return count

"""
Time Complexity:  O(m + n)
Space Complexity: O(1)
"""
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row, column, count = len(grid) - 1, 0, 0

        while row >= 0 and column < len(grid[0]):
            if grid[row][column] < 0:
                row -= 1
                count += (len(grid[0]) - column)
            else:
                column += 1

        return count



Solution().countNegatives([[7, -3]])
Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
Solution().countNegatives([[3,2], [1,0]])