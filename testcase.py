#费布那切数列，求第N个数字
# def fabrec(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#
#     return fabrec(n-1)+fabrec(n-2)
#
#
# def fabdp(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     if n > 2:
#         a = 0
#         b = 1
#         for _ in range ( 3, n + 1):
#             temp = a + b
#             a = b
#             b = temp
#     return temp
#
#
#
#
#
# # 0 1 1 2 3
#
#
# print(fabrec(10))
#
# print(fabdp(10))

# s = "abcdef"
# print(s.find("b"))
# print(s[0:s.find("b")])
# s = s[0:s.find("b")]+"!"+s[s.find("b")+1:]
#
# # print(s)
#
# re = [[1]] * 5
# print(1 <= 1 < 3)
#
# n = 10
# dic = {n:0 for n in range(n)}
# print(dic)

# class Solution:
#     """
#     @param str: The identifier need to be judged.
#     @return: Return if str is a legal identifier.
#     """
#
#     def isLegalIdentifier(self, str):
#         # Write your code here.
#         if not str:
#             return False
#
#         if str[0].isdigit():
#             return False
#
#         for i in range(1, len(str) - 1):
#             if not (s[i].isalnum() or s[i] == "_"):
#                 return False
#
#         return True
print([i for i in range(1,10)])