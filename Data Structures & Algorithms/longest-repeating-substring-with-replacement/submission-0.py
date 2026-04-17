class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            ch = s[right]
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
            
            if freq[ch] > max_freq:
                max_freq = freq[ch]

            while(right-left+1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right-left+1)
        return max_len