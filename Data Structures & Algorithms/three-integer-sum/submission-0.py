class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        
        out = []
        for i in range(len(sorted_nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            
            l = i + 1
            r = len(sorted_nums) - 1

            while l < r:
                current_sum = sorted_nums[l] + sorted_nums[r] + sorted_nums[i]

                if current_sum == 0 :
                    out.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l = l + 1
                    r = r - 1

                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1
                    while l < r and sorted_nums[r] == sorted_nums[r + 1]:
                        r -= 1
                elif current_sum < 0 :
                    l += 1
                else :
                    r -= 1
        return out
                


           
            