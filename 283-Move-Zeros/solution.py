class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        i = 0
        for j in range(n):
            if (nums[j] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        return nums

solution = Solution()

print(solution.moveZeroes([0, 0, 1, 1]))