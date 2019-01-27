class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    141. x的平方根
    实现 int sqrt(int x) 函数，计算并返回 x 的平方根。

    样例
    sqrt(3) = 1

    sqrt(4) = 2

    sqrt(5) = 2

    sqrt(10) = 3

    挑战
    O(log(x))
    """
    def sqrt(self, x):
        l, r = 0, x
        # write your code here
        while l + 1 < r:
            m = (r+l) // 2
            if m * m == x:
                return m
            elif m * m > x:
                r = m
            else:
                l = m
        if l * l == x:
            return l
        if r * r == x:
            return r
        return l
