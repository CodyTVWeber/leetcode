class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        running_max_length = 0
        chars = list(s)
        char_length = len(chars)
        for currentCharIndex in range(char_length):
            current_chars = chars[currentCharIndex]
            new_current_index = currentCharIndex + 1
            while new_current_index < char_length and chars[new_current_index] not in current_chars:
                current_chars += chars[new_current_index]
                new_current_index += 1
            if running_max_length < len(current_chars):
                running_max_length = len(current_chars)

        return running_max_length


solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
