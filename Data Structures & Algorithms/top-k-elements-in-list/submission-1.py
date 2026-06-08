class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for num in nums:
            if num in dct:
                dct[num] += 1
            else:
                dct[num] = 1
        heap = []
        for num in dct.keys():
            heapq.heappush(heap, (dct[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res       
            
        