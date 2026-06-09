class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_sum = 1
        count_zero = 0
        for num in nums:
            if num == 0:
                count_zero += 1
            else:
                total_sum *= num
        ans = []

        if count_zero > 1:
            return [0 for num in nums]


        for num in nums:
            if count_zero > 0:
                ans.append(total_sum if num == 0 else 0)
            else:
                ans.append(total_sum // num)
        return ans

        