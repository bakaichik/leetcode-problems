class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        i = 0
        for j in range(n):
            if (nums[j] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

solution = Solution()

print(solution.moveZeroes([0, 1, 2, 3, 4]))