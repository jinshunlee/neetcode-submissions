class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stk = []
        for pos, speed in pairs:
            stk.append((target - pos) / speed)
            if len(stk) >= 2 and stk[-2] >= stk[-1]:
                stk.pop()
        return len(stk)

        