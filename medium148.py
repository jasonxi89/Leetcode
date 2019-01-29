class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    148. 颜色分类
    给定一个包含红，白，蓝且长度为 n 的数组，将数组元素进行分类使相同颜色的元素相邻，并按照红、白、蓝的顺序进行排序。

    我们可以使用整数 0，1 和 2 分别代表红，白，蓝。

    样例
    给你数组 [1, 0, 1, 2], 需要将该数组原地排序为 [0, 1, 1, 2]。

    挑战
    一个相当直接的解决方案是使用计数排序扫描2遍的算法。

    首先，迭代数组计算 0,1,2 出现的次数，然后依次用 0,1,2 出现的次数去覆盖数组。

    你否能想出一个仅使用常数级额外空间复杂度且只扫描遍历一遍数组的算法？

    注意事项
    不能使用代码库中的排序函数来解决这个问题。
    排序需要在原数组中进行。

    """
    # def sortColors(self, nums):
        # write your code here
        # 实现000011112222  0120201021012,    021
        # 3个指针，一起往右移动？如果第一个非0数开始，如果是2，就移动2号指针去换？如果是3，就移动3号指针去换？
        # 不知道哪里有问题，不过重新想了个，用2个指针，一个count,左右开始晃悠，左边如果遇到非0判断，如果是1，改count,右边如果是1，改coumt,等2个指针+count=len()，停止
        # nlens = len(nums)
        # count = 0
        # l, r = 0 , 0
        # while l + r + count <= nlens:
        #     if nums[l] == 1:
        #         nums [l] == 0
        #         count += 1
        #         print("1变0，count+1", l, count)
        #         l += 1
        #     elif nums[l] == 0:
        #         l += 1
        #     else:
        #         #这个时候nums [l] ==2
        #         while l + r + count <= nlens:
        #             if nums[nlens - 1 - r] == 0:
        #                 print("置换前",nums,l,r,count)
        #                 nums[l], nums[nlens - 1 - r] = nums[nlens - 1 - r], nums[l]
        #                 print("置换后",nums,l,r,count)
        #                 r += 1
        #                 l += 1
        #                 break
        #             elif nums[nlens - 1 - r] == 1:
        #                 nums[nlens - 1 - r] = 2
        #                 count +=1
        #                 r += 1
        #                 print("2变0，count+1", nlens - 1 - r, count)
        #             else:
        #                 r += 1
        #
        # print(l,r,count,nlens)
        # for n in range(l - 1, l+count -1):
        #     print(n)
        #     nums[n] = 1
        # return nums
        #第一次尝试，临界值出现了问题，其实老师的方法最巧妙，mid来移动，左右丢0和2，当时想的是过了后1还在左边，但是后来一想这么过了遍以后，左边只有0和1，右边只有2，因为动的是右指针
        #所以他还会原地在判断一次，判断缓过来的是0还是1。机智啊！！


    def sortColors(self, A):
        left, index, right = 0, 0, len(A) - 1

        # be careful, index < right is not correct
        while index <= right:
            if A[index] == 0:
                A[left], A[index] = A[index], A[left]
                left += 1
                index += 1
            elif A[index] == 1:
                index += 1
            else:
                A[right], A[index] = A[index], A[right]
                right -= 1

if __name__ == "__main__":
    print(Solution.sortColors(Solution,[2,0,2,2,1,2,2,1,2,0,0,0,1]))
    print([0,0,0,0,1,1,1,2,2,2,2,2,2])





