class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """

    def longestPalindrome(s):
        if not s:
            return ""

        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

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
