class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums :
            count[n] = count.get(n, 0) + 1
        li = []
        sorted_item = sorted(
            count.items(), key = lambda item : item[1],
            reverse = True
        ) 
        return [key for key, value in sorted_item[:k]]