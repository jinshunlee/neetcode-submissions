class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for i in range(0, len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stk.append(s[i])
            elif s[i] == ')' or s[i] == ']' or s[i] == '}':
                item = stk and stk[-1]
                if not item:
                    return False
                else:
                    if s[i] == ')' and item == '(' or s[i] == ']' and item == '[' or s[i] == '}' and item == '{':
                        stk.pop()
                    else:
                        return False
        return len(stk) == 0



            
        