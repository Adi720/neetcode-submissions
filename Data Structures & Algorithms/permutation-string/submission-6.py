class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq1 = {}
        freq2 = {}

        for i in range(len(s1)):
            ch1 = s1[i]
            ch2 = s2[i]

            if ch1 in freq1:
                freq1[ch1] += 1
            else:
                freq1[ch1] = 1

            if ch2 in freq2:
                freq2[ch2] += 1
            else:
                freq2[ch2] = 1
        if freq1 == freq2:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            ch = s2[right]
            if ch in freq2:
                freq2[ch] += 1
            else:
                freq2[ch] = 1

            # remove old char
            left_char = s2[left]
            freq2[left_char] -= 1
            if freq2[left_char] == 0:
                del freq2[left_char]
            left += 1

            if freq1 == freq2:
                return True
        return False