class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_streak = 0

        for num in nums:
            if (num - 1) not in numSet:
                curr_streak = 1
                while (num + curr_streak) in numSet:
                    curr_streak += 1
                max_streak = max(max_streak, curr_streak)

        return max_streak

