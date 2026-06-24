class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = nums[0]
        currMax = nums[0]
        currMin = nums[0]

        for i in range(1, len(nums)):
            temp = currMax
            currMax = max(nums[i], currMax*nums[i], currMin*nums[i])
            currMin = min(nums[i], temp*nums[i], currMin*nums[i])
            maxi = max(maxi, currMax)
        return maxi