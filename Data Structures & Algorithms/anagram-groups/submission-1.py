class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        group = defaultdict(list)
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord('a')] += 1
            #Converting to tuple as key should be immutable 
            group[tuple(count)].append(word)

        result = list(group.values())
        return result
        