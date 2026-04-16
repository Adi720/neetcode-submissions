class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        items = list(freq.items())

        items.sort(key=lambda x:x[1], reverse=True)
        result = []

        for i in range(k):
            result.append(items[i][0])

        return result
        