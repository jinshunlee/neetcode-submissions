class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str = []
        for s in strs:
            sorted_str.append("".join(sorted(s)))
        lst = []
        dct = {}
        for i in range(0, len(sorted_str)):
            if sorted_str[i] in dct:
                dct[sorted_str[i]].append(strs[i])
            else:
                dct[sorted_str[i]] = [strs[i]]
        ans = []
        for key in dct:
            ans.append(dct[key])
        return ans
        