class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array

    160. 寻找旋转排序数组中的最小值 II
    假设一个旋转排序的数组其起始位置是未知的（比如0 1 2 4 5 6 7 可能变成是 6 7 0 1 2 3 4 5）。

    你需要找到其中最小的元素。

    数组中可能存在重复的元素。

    样例
    给出[4,4,5,6,7,0,1,2]  返回 0

    注意事项
    The array may contain duplicates.
    """
    def findMin(self, nums):
        # write your code here
        # return min(nums) 哈哈哈哈哈
        # 查看中间的数字，如果中间数字比末位大，那么查中间的右边的数字，如果中间的比末尾小末尾的数字移动过来，结束的时候，返回的其实就是start = end = 最小值

        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid
            else:
                end = end - 1
        return nums[start]

