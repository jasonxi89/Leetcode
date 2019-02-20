class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):
        # write your code here
        nums = sorted(nums)
        result = []
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, startindex, path, result):
        result.append(path[:])
        for i in range(startindex, len(nums)):
            if i != startindex and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.dfs(nums, i + 1, path, result)
            path.pop()