class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)

        total_product = 1
        for num in nums:
            if num != 0:
                total_product *= num
        result = []
        for num in nums:
            if zero_count == 1:
                if num == 0:
                    result.append(total_product)
                else:
                    result.append(0)
            else:
                result.append(total_product//num)

        return result