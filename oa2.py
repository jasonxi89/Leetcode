def longestPalindromeSubseq(s):
    # Write your code here
    length = len(s)
    if length == 0:
        return 0
    dp = [[0 for _ in range(length)] for __ in range(length)]
    for i in range(length - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, length):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][length - 1]


if __name__ =="__main__":
    longest = 0
    words = "aaaa"
    if len(words) == 2:
        print(1)
    for i in range(1, len(words)-1):
        left, right = longestPalindromeSubseq(words[0:i]), longestPalindromeSubseq(words[i:])
        temp = left * right
        if temp > longest:
            longest = temp
    print(longest)
