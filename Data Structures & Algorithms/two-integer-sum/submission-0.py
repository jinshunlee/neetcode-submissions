class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in table and i != table[complement]:
                return [min(i, table[complement]), max(i, table[complement])]
            table[nums[i]] = i        