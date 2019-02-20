class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        nums.sort()
        result = []
        self.dfs(nums, 0, [], result)
        return result


    #返回子集，那么我们从头开始判断就完事了？
    def dfs(self, numns, startindex, path, result):
        result.append(path[:])
        for i in range (startindex, len(numns)):
            path.append(numns[i])
            self.dfs(numns, i+1, path, result)
            path.pop()