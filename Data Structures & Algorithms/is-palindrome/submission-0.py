import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s)
        start = 0
        end = len(cleaned) - 1
        while start < end:
            if cleaned[start].lower() != cleaned[end].lower():
                return False
            start += 1
            end -= 1
        return True

