class Solution:
    """
    @param num: An integer
    @return: an integer array

    235. 分解质因数
    将一个整数分解为若干质因数之乘积。

    样例
    样例 1：

    输入：10
    输出：[2, 5]
    样例 2：

    输入：660
    输出：[2, 2, 3, 5, 11]
    注意事项
    你需要从小到大排列质因子。
    """
    def primeFactorization(self, num):
        # write your code here
        import math
        end = int(math.sqrt(num))+1


        def helper(num, end):
            for w in range(2,end):
                if num % w ==0:
                    return w
                if w == end:
                    return None


        re=[]
        while helper(num, end) != None:
            re.append(helper(num, end))
            num = num / helper(num, end)

        re.append(int(num))
        return re

if __name__ =="__main__":
    print(Solution.primeFactorization(Solution, 10))
