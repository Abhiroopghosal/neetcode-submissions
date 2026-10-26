class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for n in nums_set:
            if n - 1 not in nums_set:
                current = 1
                while n + current in nums_set:
                    current += 1
                longest = max(current, longest)
                
        return longest