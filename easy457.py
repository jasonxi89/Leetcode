class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    457. 经典二分查找问题
    在一个排序数组中找一个数，返回该数出现的任意位置，如果不存在，返回-1

    样例
    给出数组 [1, 2, 2, 4, 5, 5].

    对于 target = 2, 返回 1 或者 2.
    对于 target = 5, 返回 4 或者 5.
    对于 target = 6, 返回 -1.
    挑战
    O(logn) 的时间
    """

    def findPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid

        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        return -1