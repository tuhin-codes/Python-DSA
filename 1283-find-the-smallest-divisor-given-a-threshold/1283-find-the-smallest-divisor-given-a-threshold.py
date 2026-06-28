class Solution:

    def findSum(self, nums, divisor):

        total = 0

        for num in nums:
            total += (num + divisor - 1) // divisor

        return total

    def smallestDivisor(self, nums, threshold):

        low = 1
        high = max(nums)

        ans = high

        while low <= high:

            mid = (low + high) // 2

            if self.findSum(nums, mid) <= threshold:

                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans