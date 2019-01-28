class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    604. 滑动窗口内数的和
    给你一个大小为n的整型数组和一个大小为k的滑动窗口，将滑动窗口从头移到尾，输出从开始到结束每一个时刻滑动窗口内的数的和。

    样例
    对于数组 [1,2,7,8,5] ，滑动窗口大小k= 3 。
    1 + 2 + 7 = 10
    2 + 7 + 8 = 17
    7 + 8 + 5 = 20
    返回 [10,17,20]
    """
    def winSum(self, nums, k):
        # write your code here
        if not nums:
            return 0
        if k > len(nums):
            k = len(nums)
        l, r = 0, k -1
        ret = []
        for base in range(0,len(nums)- k + 1):
            ret.append(sum(nums[i] for i in range(base +l,base + r + 1)))
        return ret


if __name__ =="__main__":
    print(Solution.winSum(Solution,[1,2,7,8,5],3))