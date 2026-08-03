class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []
        for idx, t in enumerate(temperatures):
            while stk and t > stk[-1][1]:
                stkIdx, _ = stk.pop()
                res[stkIdx] = idx - stkIdx
            stk.append([idx, t])
        return res
                 
        