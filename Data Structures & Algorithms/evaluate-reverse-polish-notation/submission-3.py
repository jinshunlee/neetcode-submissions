class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for elem in tokens:
            if elem == '-':
                r = int(stk.pop())
                l = int(stk.pop())
                stk.append(l - r)
            elif elem == '+':
                r = int(stk.pop())
                l = int(stk.pop())
                stk.append(l + r)
            elif elem == '/':
                r = int(stk.pop())
                l = int(stk.pop())
                stk.append(int(l / r))
            elif elem == '*':
                r = int(stk.pop())
                l = int(stk.pop())
                stk.append(l * r)
            else:
                stk.append(int(elem))
        return stk[0]
            
                




        