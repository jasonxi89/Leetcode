class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    521. 去除重复元素
    给一个整数数组，去除重复的元素。

    你应该做这些事

    1.在原数组上操作
    2.将去除重复之后的元素放在数组的开头
    3.返回去除重复元素之后的元素个数

    样例
    例1:

    输入:
    nums = [1,3,1,4,4,2]
    输出:
    [1,3,4,2,?,?]
    4
    Explanation:

    Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
    Return the number of unique integers in nums => 4.
    Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.
    例2:

    输入:
    nums = [1,2,3]
    输出:
    [1,2,3]
    3
    挑战
    1.O(n)时间复杂度.
    2.O(nlogn)时间复杂度但没有额外空间
    注意事项
    不需要保持原数组的顺序
    挑战1就直接搞个字典去重
    挑战2拷贝数组
    """

    # O(n) time, O(n) space
    class Solution:
        # @param {int[]} nums an array of integers
        # @return {int} the number of unique integers
        def deduplication(self, nums):
            # Write your code here
            d, result = {}, 0
            for num in nums:
                if num not in d:
                    d[num] = True
                    nums[result] = num
                    result += 1

            return result

    # O(nlogn) time, O(1) extra space
    class Solution:
        # @param {int[]} nums an array of integers
        # @return {int} the number of unique integers
        def deduplication(self, nums):
            # Write your code here
            n = len(nums)
            if n == 0:
                return 0

            nums.sort()
            result = 1
            for i in xrange(1, n):
                if nums[i - 1] != nums[i]:
                    nums[result] = nums[i]
                    result += 1

            return result