#two pointer, left - > right, right -> left.
def isPalindrome(self, s):
    # write your code here
    if s == "" or len(s) == 0:
        return True
    leftpointer = 0
    rightpointer = len(s) - 1
    s = s.lower()
    while leftpointer <= rightpointer:
        while (not s[leftpointer].isalnum()) and leftpointer < rightpointer:
            leftpointer += 1
        while (not s[rightpointer].isalnum()) and leftpointer < rightpointer:
            rightpointer -= 1
        if s[leftpointer] != s[rightpointer]:
            return False
        leftpointer += 1
        rightpointer -= 1
        if leftpointer >= rightpointer:
            break
    return True