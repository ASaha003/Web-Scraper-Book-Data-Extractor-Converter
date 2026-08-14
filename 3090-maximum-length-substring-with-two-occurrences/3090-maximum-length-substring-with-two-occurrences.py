class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        char_count = {}

        for right in range(len(s)):
            # Add the current character to our frequency map
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            # If the current character appears more than twice, 
            # shrink the window from the left until it's valid again
            while char_count[s[right]] > 2:
                char_count[s[left]] -= 1
                left += 1

            # Update the maximum length found so far
            max_length = max(max_length, right - left + 1)

        return max_length