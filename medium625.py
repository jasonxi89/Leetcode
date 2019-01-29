class Solution:
    """
    @param nums: an integer array
    @param low: An integer
    @param high: An integer
    @return: nothing
    625. 数组划分II
        将一个没有经过排序的整数数组划分为 3 部分:
        1.第一部分中所有的值都 < low
        2.第二部分中所有的值都 >= low并且 <= high
        3.第三部分中所有的值都 > high
        返回任意一种可能的情况。

        样例
        给出数组 [4,3,4,1,2,3,1,2] ，low = 2，high = 3。
        变为 [1,1,2,3,2,3,4,4]
        ([1,1,2,2,3,3,4,4] 也是正确答案，但 [1,2,1,2,3,3,4,4] 不是)

        挑战
        1.在原地完成
        2.用一个循环完成

        注意事项
        在所有测试数组中都有 low <= high。

        和184一样，分成三个数组的时候，左右只负责标记已经处理完的数字，只动中间的：如果小于LOW，那就值互换，如果大于HIGH，就换值，再次判断过来的值是小于还是大于等于
        l和index之间是什么？就是<= 和 <的差集
    """
    def partition2(self, nums, low, high):
        # write your code here
        l, index, r = 0, 0, len(nums) -1
        while index <= r :
            if nums[index] < low:
                nums[index], nums[l] = nums[l], nums[index]
                index += 1
                l += 1
            elif nums[index] >= low and nums[index] <= high:
                index += 1
            else:
                nums[r],nums[index] = nums[index],nums[r]
                r -= 1





