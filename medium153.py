class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here

        #sort the num for the low -> high
        num.sort()
        result = []
        current = []
        self.dfs(num,0,target,current,result)
        return result
    #递归的定义，
    def dfs(self, num, startindex, target,current, result):
        #递归的出口：如果target是0，写入result
        if target == 0:
            # result.append(list(current))
            #两种方法都可以，都是类似于deepcopy
            result.append(current[:])
            return

        #遍历0到最后一个数字，看看是不是比target小
        for i in range(startindex,len(num)):
            if num[i]> target:
                break
            if i!=startindex and num[i-1]==num[i]:
                continue

            current.append(num[i])
            self.dfs(num,i+1,target-num[i],current,result)
            current.pop()



