class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str +=  f"{len(s)}#{s}"
        print('encoded_str:', encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        ans = []
        length_str = ''
        i = 0
        while i < len(s):
            if s[i] == '#':
                length = int(length_str)
                ans.append(s[i+1:i+length+1])
                length_str = ''
                i += length + 1
            else:
                length_str += s[i]
                i += 1
        return ans


  
        
