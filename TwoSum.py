# Brute Force
# Time Complexity: O(n^2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            print(i)
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
                
# Hash Map
# Time Complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                return [hash_map[target - nums[i]], i]
            hash_map[nums[i]] = i