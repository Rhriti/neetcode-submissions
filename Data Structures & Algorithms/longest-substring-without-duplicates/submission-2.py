class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        index = {}
        i = 0
        maxs = 0
        
        for j in range(len(s)):
            # If we've seen this character AND it's inside our current window
            if s[j] in index and index[s[j]] >= i:
                # Jump the left pointer straight past the duplicate
                i = index[s[j]] + 1
            
            # Update the character's most recent index
            index[s[j]] = j
            
            # Calculate max length (using a simple if-statement is faster than max() in Python)
            current_length = j - i + 1
            if current_length > maxs:
                maxs = current_length
                
        return maxs