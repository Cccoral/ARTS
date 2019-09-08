# 题目描述
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 注意 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231, 231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

# 1.正整数 <2^31-1  正整数后有0的情况
# 2.负整数 >-2^31   负整数后有0的情况
# 3.0

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
            """
        s = ''
        x = str(x)
        for i in range(len(x)):
            if x[0] == '-':
                if i == 0:
                    s += '-'
                elif x[-i] == 0:
                    if x[-i + 1] != 0:
                        s += x[-i]
                    else:
                        s = '0'
                else:
                    s += x[-i]
            else:
                if x[-(i + 1)] != 0:
                    s += x[-(i + 1)]
                elif x[-i] != 0:
                    s += x[-(i + 1)]
                else:
                    s = '0'
        s=int(s)
        if s >= -(2 ** 31) and s <= (2 ** 31 - 1):
            return s
        else:
            return 0

# so = Solution()
# print(so.reverse(1534236469))

# 执行用时 :
# 52 ms , 在所有 Python 提交中击败了 5.97%的用户
# 内存消耗 : 11.6 MB , 在所有 Python 提交中击败了 34.10% 的用户

# 参考一：class Solution(object):
# 本题的思路就是先判断给定整数x的正负情况，把符号首先给提取出来
# 然后将abs(x)变成字符串，接着将字符串反转，最后恢复成整数
# 整数-》字符串-》反转=》整数
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         # 定义用来标记给定整数x的正负情况，若x>=0， 则flag=1；反之，则flag=-1
#         flag = 1 if x >= 0 else -1
#         abs_x = abs(x)
#         # 将abs(x)变成字符串
#         x_str = str(abs_x)
#         # 将字符串x_str反转
#         reverse_x_str = x_str[::-1]
#         # 最后恢复成整数
#         reverse_x_int = int(reverse_x_str) * flag
#         if -2 ** 31 <= reverse_x_int <= 2**31 - 1:
#             return reverse_x_int
#         else:
#             return 0
#
#
# if __name__ == "__main__":
#     x = 231
#     reverse_x = Solution().reverse(x)
#     print(reverse_x)

#参考二：数字直接进行算术运算 不需要转换
#  class Solution:
#     def reverse(self, x: int) -> int:
#         y, res = abs(x), 0
#         of = (1 << 31) - 1 if x > 0 else 1 << 31
#         while y != 0:
#             res = res * 10 + y % 10
#             if res > of: return 0
#             y //= 10
#         return res if x > 0 else -res
#
# 算数 取尾数-》公式-》新数
# print(-113//10)
# print（113//10）不一样
# print(2**31)
# print(1<<31)
# print(1<<2)
# print((1<<31)-1)
# 涉及到原码补码问题


# 参考三：数字直接进行算术运算 不需要转换
# class Solution :
#     def reverse(self,x):
#         rev = 0
#         while(x != 0):
#             pop = int(x % 10)
#             x = int(x / 10)
#             if(rev > int((2**31-1) / 10 )or (rev == int((2**31-1)/ 10) and pop > int((2**31-1) % 10))):
#                 rev = 0
#                 break
#             elif(rev < int((-2**31) / 10) or (rev == int((-2**31)/ 10) and x < int((-2**31) % 10))):
#                 rev = 0
#                 break
#             rev = rev * 10 + pop
#         return rev

# python有个特性：自动扩容
# Python： 存储数字理论上是无限长度，因此每次计算完后判断res与of的大小即可；
# Java： 数字计算会溢出，因此要判断res和of / 10的大小关系（即确定再添 11 位一定会溢出）。



