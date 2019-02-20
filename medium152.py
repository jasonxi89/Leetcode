class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):

        #1到N，K个数
        # write your code here
        if  k >= n:
            return [i for i in range(1,n+1)]
        result = []
        self.dfs(n,1, k, [], result)
        return result
    #递归的定义，n表示最大数，startnumer表示开始的个数，k表示剩余多少个数字,path表示现在的样子，result来接收值
    def dfs(self,n, startnumber, k, path, result):
         #如果不剩下数字，直接深度拷贝
         if k == 0:
             result.append(path[:])
             return
         for i in range(startnumber, n + 1):
             path.append(i)
             self.dfs(n, i+1, k-1, path, result)
             path.pop()


if __name__ =="__main__":
    print(Solution.combine(Solution,2,1))