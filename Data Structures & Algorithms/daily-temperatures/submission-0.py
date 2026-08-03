class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []
        for idx, t in enumerate(temperatures):
            while stk and t > stk[-1][1]:
                idxVal, _ = stk.pop()
                res[idxVal] = idx - idxVal
            stk.append([idx, t])
        return res
                 
        