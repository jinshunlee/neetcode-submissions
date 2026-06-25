class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
        longest = 0
        for val in seen:
            if val - 1 not in seen:
                length = 1
                while val + length in seen:
                    length = length + 1
                longest = max(longest, length)
        return longest

        