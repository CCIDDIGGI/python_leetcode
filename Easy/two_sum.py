# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

from typing import List


class Solution:
    def two_sum(nums: List[int], target: int) -> List[int]:
        # O(n2) Complexity - Runtime 1403, Memory 17,44
        # for i, x in enumerate(nums):
        #     for y in range(i + 1, len(nums)):
        #         if (x + nums[y]) == target:
        #             return [i, y]

        # O(n) Complexity - Runtime 49, Memory 17,61
        index_num_map = {}

        for i, num in enumerate(nums):
            difference = target - num

            if difference in index_num_map:
                return [index_num_map[difference], i]
            
            index_num_map[num] = i
        
        return []

                    
x = Solution

y = x.two_sum([2,7,11,15], 9)

print(y)