class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    在数组中找到第k大的元素

    样例
    给出数组 [9,3,2,4,8]，第三大的元素是 4

    给出数组 [1,2,3,4,5]，第一大的元素是 5，第二大的元素是 4，第三大的元素是 3，以此类推

    挑战
    要求时间复杂度为O(n)，空间复杂度为O(1)

    注意事项
    你可以交换数组中的元素的位置
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        nums.sort()
        return nums[len(nums)-n]
        #？？？？？？？黑人问号脸