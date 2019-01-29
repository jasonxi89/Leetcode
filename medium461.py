class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    461. 无序数组K小元素
    找到一个无序数组中第K小的数

    样例
    [3, 4, 1, 2, 5], k = 3, 第三小的数是3

    挑战
    O(nlogn)的非常简单，是否可以O(n)
    """
    def kthSmallest(self, k, nums):
        # write your code here
        # nlogn就是先sort再遍历？
        # 回家看选择排序！
        pass