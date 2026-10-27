class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ''.join(i.lower() for i in s if i.isalnum())
        print(strs)
        left = 0
        right = len(strs) - 1

        while left < right:
            if strs[left] != strs[right]:
                return False
            left += 1
            right -= 1
        return True