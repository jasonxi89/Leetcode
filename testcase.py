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
# # print([i for i in range(1,10)])
# # print("abcd".rfind("e"))
# cut = "1+2+3-3+4+5"
# num = 0
#
# for i in range(len(cut) - 1, 0, -1):
#     if cut[i] == "+":
#         num += int(cut[i + 1:])
#         cut = cut[:i]
#     elif cut[i] == "-":
#         num -= int(cut[i + 1:])
#         cut = cut[:i]
# num += int(cut)
#
# print(num)


# input = ['aaabbb', 'bbbaaa']
# res = ''
# dict1 ={}

# #predix是每个INPUT的后3个
# predix = [i[-3:] for i in input]
#
#
# for word in input:
#     dict1[word[0:3]] = word[3:]
#     if word[0:3] not in predix:
#         res = word
# if res != None:
#     res = word
#
# while dict1.get(res[-3:]) != None:
#     temp  = res[-3:]
#     res += dict1[res[-3:]]
#
# print(res)
#思路，递归，然后把东西丢进去
# def questiontwo(input):
#     result = []


def dfs(path,input):
    if len(input) <=1:
        return input[0]
    curr = input[-1]
    input.pop()
    for i in range(len(input)):
        if curr[-3:] == input[i][0:3]:
            input[i] = curr + input[i][3:]
        elif curr[0:3] == input[i][-3:]:
            input[i] += curr[3:]
    return dfs(input)

if __name__ == "__main__":
    # input = ['aaabbb', 'bbbaaa']
    # input = ['AGTGGGGGGGGG', 'AAACCCAATTT', 'TTTACACAGCT', 'GCTGGGCCCAGT']
    # res = ''
    # dict1 ={}
    # predix = [i[-3:] for i in input]
    #
    #
    # for word in input:
    #     dict1[word[0:3]] = word[3:]
    #     if word[0:3] not in predix:
    #         res = word
    #
    #
    # while dict1.get(res[-3:]) != None:
    #     temp  = res[-3:]
    #     res += dict1[res[-3:]]
    #     dict1.pop(temp)
    #
    #
    # print(res)
    # dict = {"a":1,"b":2,"d":5,"c":3}
    from operator import itemgetter
    # dict= [2,5,46,23,9,78]
    # # dict1 = sorted(dict, key=lambda x:x[1])
    # # dict1 = sorted(dict, key=itemgetter(1))
    # dict2 = list(enumerate(dict))
    # dict3 = sorted(dict2, key = lambda x:x[1])
    # print(type(dict2))
    # print(dict2)
    # print(type(dict3))
    # print(dict3)
    # str = "i love you   you love me"
    # print("-".join(str.split(" ")))
    str = "TTTAAATTTGGGAAA"
    map_dic = {"AAA":"A","TTT":"T","GGG":"G"}
    from collections import Counter
    freq = Counter()
    for i in range(0,len(str),3):
        if str[i:i+3] in map_dic:
            freq[str[i:i+3]] += 1
    # print(sorted(freq.items,key=lambda freq:freq[0]))
    print(freq)
    freq = sorted(freq.items(),key=lambda  x:x[0])
    print(freq)






