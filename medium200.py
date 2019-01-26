class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    #方法1：动态规划，思想就是把一个问题从大方向拆解到小的方面，也可以说递归是从大到小，动态规划是从小到大
    def longestPalindrome(s):
        if not s:
            return ""

        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        #生成数组，当比较某一个点的时候，True。
        #for i in range(1, n):
        #    is_palindrome[i][i - 1] = True
        #这个就是防止比较相邻2位出问题，先做的边界处理
        for i in range(n):
            is_palindrome[i][i] = True
        for i in range(1, n):
            is_palindrome[i][i - 1] = True

        longest, start, end = 1, 0, 0
        #length是这个回文串多长
        #i这个回文串可以起始的位置
        for length in range(1, n):
            for i in range(n - length):
                #j是结束位置(开始位置+长度)
                j = i + length
                #开始位置+结束位置的表示 = 开始位置和结束位置相等，而且上一个相等
                is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i + 1][j - 1]
                if is_palindrome[i][j]:
                    longest = length
                    start, end = i, j

        return s[start:end + 1]


if __name__ == '__main__':
    print(Solution.longestPalindrome("aaaabbbbbbbccccccccc"))

# 方法2：中心暴力枚举：
#
# class Solution:
#     """
#     @param s: input string
#     @return: the longest palindromic substring
#     """
#
#     def longestPalindrome(self, s):
#         if not s:
#             return ""
#
#         longest = ""
#         for middle in range(len(s)):
#             sub = self.find_palindrome_from(s, middle, middle)
#             if len(sub) > len(longest):
#                 longest = sub
#             sub = self.find_palindrome_from(s, middle, middle + 1)
#             if len(sub) > len(longest):
#                 longest = sub
#
#         return longest
#
#     def find_palindrome_from(self, string, left, right):
#         while left >= 0 and right < len(string) and string[left] == string[right]:
#             left -= 1
#             right += 1
#
#         return string[left + 1:right]