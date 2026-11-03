class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_count = 0
        window = set()

        for right in range(len(s)):

            while s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])

            max_count = max(max_count, right - left + 1)

        return max_count