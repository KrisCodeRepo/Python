# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_num = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in index_num:
                return [index_num[complement], index]
            index_num[num] = index
        return []
from typing import List

# Example usage:
# solution = Solution()
# result = solution.twoSum([2, 7, 11, 15], 9)

# print(result)  # Output: [0, 1]
# Example usage:
# solution = Solution()             
# result = solution.twoSum([3, 2, 4], 6)
# print(result)  # Output: [1, 2]
        