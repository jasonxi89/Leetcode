class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    617. 最大平均值子数组 II
    给出一个整数数组，有正有负。找到这样一个子数组，他的长度大于等于 k，且平均值最大。

    样例
    给出 nums = [1, 12, -5, -6, 50, 3], k = 3

    返回 15.667 // (-6 + 50 + 3) / 3 = 15.667

    注意事项
    保证数组的大小 >= k


    3 4 8 1 100 2
    """

    # def maxAverage(self, nums, k):
    #     # write your code here
    #     if not nums:
    #         return None
    #     # find the biggest number, record the position
    #     max = nums[0]
    #     pos = [];
    #     for n in range(len(nums)):
    #         if nums[n] > max:
    #             pos = [n]
    #             max = nums[n]
    #         elif nums[n] == max:
    #             pos.append(n)
    #
    #     print("最大值是",max)
    #     print("存在位置",pos)
    #
    #     # position 3, k = 2,l = 2, r 3
    #     # print(pos)
    #     def helper(pos, nums, k):
    #         # 调整位置
    #         l = pos - k + 1
    #         r = pos
    #         while l < 0:
    #             l += 1
    #             r += 1
    #         while r > len(nums):
    #             l -= 1
    #             r -= 1
    #         print(l, r)
    #         sum = 0
    #         for n in range(l, r + 1):
    #             sum += nums[n]
    #         avg = sum / k
    #         # print()
    #         # 如果左右有数字，循环比较，先比较大的
    #         # if l -1 > -1 and r + 1 < len(nums):
    #         #
    #         while True:
    #             print(l, " ", r, " ", sum, " ", avg)
    #             if l - 1 > -1 and nums[l - 1] >= avg and (r + 1 > len(nums) - 1 or nums[l - 1] >= nums[r + 1]):
    #                 print("左移1位")
    #                 sum += nums[l - 1]
    #                 k += 1
    #                 avg = sum / k
    #                 l -= 1
    #                 print("SUM是", sum, "K是", k, "AVG是", avg, "l是", l)
    #             if r + 1 < len(nums) and nums[r + 1] >= avg and (l - 1 < 0 or nums[r + 1] >= nums[l - 1]):
    #                 print("右移一位")
    #                 sum += nums[r + 1]
    #                 k += 1
    #                 avg = sum / k
    #                 r += 1
    #                 print("SUM是", sum, "K是", k, "AVG是", avg, "r是", r)
    #             if (l - 1 < 0 or nums[l - 1] < avg) and (r + 1 > len(nums) - 1 or nums[r + 1] < avg):
    #                 print(l - 1 < 0,nums[l - 1] < avg,l - 1 < 0 or nums[l - 1] < avg)
    #                 print()
    #                 print("秒了")
    #                 break
    #         return avg
    #
    #     maxes = []
    #
    #     for num in pos:
    #         maxes.append(helper(num, nums, k))
    #
    #     max = maxes[0]
    #     for nums in maxes:
    #         if nums > max:
    #             max = nums
    #
    #     return max
    #整个思路想偏了，果然是要用那个不知名的数列，先减去平均数，然后再算
    #九章同学的思路
    #初看是一道普通的prefixSum题
    # 但考察的prefixSum的剪枝
    #
    # 1.初级解法：
    # 求出prefixSum,通过遍历所有可能的substring
    # 打擂台的方式 求出(prefixSum[i] - prefixSum[j]) / (j - i) 的最小值
    # 由于这个最小值中起决定性作用的有两个条件(prefixSum[i] - prefixSum[j]) 和(j - i)
    # 所以无法用全循环保存最小值的情况来减枝,只能全部遍历所以.
    # 时间复杂度即为完整遍历prefixSum: O(n^2)
    #
    # 2.高级解法：
    # 即假设我们要求的平均值为target，当所有数同时减去target，我们可以去掉(j - i) 这个条件
    # 因为当对所有数同时减去target时，/(j - i) 就变得没有意义了，我们只在乎大于0还是小于0
    #
    # 这样，我们的问题就可以转化为用二分法来寻找满足 target 最大 且满足有subrange为0的target，prefix 仅用作判断条件
    # 时间复杂度为O(nlgn)

    #九章老师的解释
    # 使用九章算法强化班中讲过的基于二分答案的方法
    # 二分出average之后，把数组中的每个数都减去average，然后的任务就是去求这个数组中，是否有长度 >= k的subarray，他的和超过
    # 0。
    # 这一步用类似Maximumubarray的解法来做就好了
    #'''
    # 下面来看一种优化时间复杂度到O(nlg(max - min))
    # 的解法，其中max和min分别是数组中的最大值和最小值，是利用了二分搜索法，博主之前写了一篇LeetCode
    # Binary
    # Search
    # Summary
    # 二分搜索法小结的博客，这里的二分法应该是小结的第四类，也是最难的那一类，因为判断折半的方向是一个子函数，这里我们没有用子函数，而是写
    # 到了一起，可以抽出来成为一个子函数，这一类的特点就是不再是简单的大小比较，而是需要一些复杂的操作来确定折半方向。这里主要借鉴了蔡文森
    # 特大神的帖子，所求的最大平均值一定是介于原数组的最大值和最小值之间，所以我们的目标是用二分法来快速的在这个范围内找到我们要求的最大平
    # 均值，初始化left为原数组的最小值，right为原数组的最大值，然后mid就是left和right的中间值，难点就在于如何得到mid和要求的最大平均值
    # 之间的大小关系，从而判断折半方向。我们想，如果我们已经算出来了这个最大平均值maxAvg，那么对于任意一个长度大于等于k的数组，如果让每个
    # 数字都减去maxAvg，那么得到的累加差值一定是小于等于0的，这个不难理解，比如下面这个数组：
    #
    # [1, 2, 3, 4]
    # k = 2
    #
    # 我们一眼就可以看出来最大平均值maxAvg = 3.5，所以任何一个长度大于等于2的子数组每个数字都减去maxAvg的差值累加起来都小于等于0，只有产
    # 生这个最大平均值的子数组[3, 4]，算出来才正好等于0，其他都是小于0的。那么我们可以根据这个特点来确定折半方向，我们通过left和right值算
    # 出来的mid，可以看作是maxAvg的一个candidate，所以我们就让数组中的每一个数字都减去mid，然后算差值的累加和，一旦发现累加和大于0了，那
    # 么说明我们mid比maxAvg小，这样就可以判断方向了。
    #
    # 我们建立一个累加和数组sums，然后求出原数组中最小值赋给left，最大值赋给right，题目中说了误差是1e - 5，所以我们的循环条件就是right
    # 比left大1e - 5，然后我们算出来mid，定义一个minSum初始化为0，布尔型变量check，初始化为false。然后开始遍历数组，先更新累加和数组
    # sums，注意这个累加和数组不是原始数字的累加，而是它们和mid相减的差值累加。我们的目标是找长度大于等于k的子数组的平均值大于mid，由于我
    # 们每个数组都减去了mid，那么就转换为找长度大于等于k的子数组的差累积值大于0。
    # 我们建立差值累加数组的意义就在于通过sums[i] - sums[j]
    # 来快速算出j和i位置中间数字之和，那么我们只要j和i中间正好差k个数字即可，然后minSum就是用来保存j位置之前的子数组差累积的最小值，所以
    # 当i >= k时，我们用sums[i - k]
    # 来更新minSum，这里的i - k就是j的位置，然后判断如果sums[i] - minSum > 0
    # 了，说明我们找到了一段长度大于等k的子数组平均值大于mid了，就可以更新left为mid了，我们标记check为true，并退出循环。在for循环外面，
    # 当check为true的时候，left更新为mid，否则right更新为mid，参见代码如下：
    # #'''

    def maxAverage(self, nums, k):
        if not nums:
            return 0

        start, end = min(nums), max(nums)
        print(start," ",end)
        while end - start > 1e-5:
            mid = (start + end) / 2
            if self.check_subarray(nums, k, mid):
                start = mid
            else:
                end = mid

        return start

    def check_subarray(nums, k, average):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num - average)

        min_prefix_sum = 0
        for i in range(k, len(nums) + 1):
            if prefix_sum[i] - min_prefix_sum >= 0:
                return True
            min_prefix_sum = min(min_prefix_sum, prefix_sum[i - k + 1])

        return False

if __name__ =="__main__":
    print(Solution.maxAverage(Solution,[1,12,-5,-6,50,3],3))