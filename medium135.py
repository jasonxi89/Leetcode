class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        #排序
        candidates.sort()
        result = []
        self.dfs(candidates,0,target,[],result)
        return result


    #递归的定义：传入数组，起始位置，目标，路径，结果
    def dfs(self,nums, startindex, target, path, result):
        if target == 0 :
            result.append(path[:])

        for i in range(startindex,len(nums)):
            if nums[i] > target:
                break
            if i != startindex and nums[i]==nums[i-1]:
                continue

            path.append(nums[i])
            self.dfs(nums, i, target-nums[i], path, result)
            path.pop()
