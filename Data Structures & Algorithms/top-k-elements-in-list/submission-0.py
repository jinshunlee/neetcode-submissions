class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for elem in nums:
            if elem in dct:
                dct[elem] += 1
            else:
                dct[elem] = 1

        freq_lst = [val[0] for val in sorted(dct.items(), key=lambda x : x[1], reverse=True)]
        return [freq_lst[i] for i in range(0, k)]

        