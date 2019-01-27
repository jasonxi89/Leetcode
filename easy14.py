class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    14. 二分查找
    给定一个排序的整数数组（升序）和一个要查找的整数target，用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。

    样例
    样例  1:
        输入:[1,4,4,5,7,7,8,9,9,10]，1
        输出: 0

        样例解释:
        第一次出现在第0个位置。

    样例 2:
        输入: [1, 2, 3, 3, 4, 5, 10]，3
        输出: 2

        样例解释:
        第一次出现在第2个位置

    样例 3:
        输入: [1, 2, 3, 3, 4, 5, 10]，6
        输出: -1

        样例解释:
        没有出现过6， 返回-1

    挑战
    如果数组中的整数个数超过了2^32，你的算法是否会出错？
    """
    def binarySearch(self, nums, target):
        # write your code here
        left, right = 0, len(nums)
        while left + 1 < right :
            mid = (left + right) // 2
            if nums[mid] < target :
                left = mid
            else :
                right = mid
        if nums[left] == target :
            return left
        elif nums[right] == target :
            return right
        return -1;
