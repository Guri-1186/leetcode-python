class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Dictionary to store the last seen index of each character
        seen = {}
        left = 0   # left side of sliding window
        max_len = 0

        for right, char in enumerate(s):
           
            if char in seen and seen[char] >= left:
                left = seen[char] + 1

            seen[char] = right

          
            max_len = max(max_len, right - left + 1)

        return max_len
    
