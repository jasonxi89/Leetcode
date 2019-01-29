class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    443. 两数之和 II
        给一组整数，问能找出多少对整数，他们的和大于一个给定的目标值。

        样例
        对于 numbers = [2, 7, 11, 15], target = 24 的情况，返回 1。因为只有11 + 15可以大于24。

        挑战
        Do it in O(1) extra space and O(nlogn) time.
    """
    def twoSum2(self, nums, target):
        # write your code here
        nums.sort()
        count, l, r = 0, 0, len(nums)-1
        while l < r:
            cur_sum = nums[l] + nums[r]
            if cur_sum > target:
                count += r - l
                r -= 1
            else:
                l += 1
        return count