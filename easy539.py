class Solution:
    """
    @param nums: an integer array
    @return: nothing

    539. 移动零
    给一个数组 nums 写一个函数将 0 移动到数组的最后面，非零元素保持原数组的顺序

    样例
    例1:

    输入: nums = [0, 1, 0, 3, 12],
    输出: [1, 3, 12, 0, 0].
    例2:

    输入: nums = [0, 0, 0, 3, 1],
    输出: [3, 1, 0, 0, 0].
    注意事项
    1.必须在原数组上操作
    2.最小化操作数
    """
    def moveZeroes(self, nums):
        # write your code here
        l , r = 0, 0
        #l标记写的位置，right找非0，当right超界限，剩下的全写0
        while r < len(nums):
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1
            r += 1
        for i in range(l, len(nums)):
            nums[i] = 0

        return nums