# 判断一个整数是否是回文数。
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# Determine whether an integer is a palindrome.
# An integer is a palindrome when it reads the same backward as forward.

# 考虑情况：
# 0 True
# 10  False
# -10113 False

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
# 第一种 转换成列表 利用reverse()倒序
        y = list(str(x))
        x = list(str(x))
        y.reverse()
        if y == x:
            return True
        else:
            return False
# 执行用时 : 44 ms, 在所有 Python 提交中击败了97.69%的用户
# 内存消耗 :11.7 MB, 在所有 Python 提交中击败了29.53% 的用户

# 第二种 转换成字符串 利用切片倒序
#         y=str(x)
#         x=str(x)
#         y = y[::-1]
#         if y == x:
#             return True
#         else:
#             return False
# 执行用时 :76 ms , 在所有 Python 提交中击败了41.39%的用户
# 内存消耗 :11.6 MB, 在所有 Python 提交中击败了33.35%的用户

# 第三种  直接数值运算 取一半位数与另一半做比较

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x = int(x / 10)
        return x == revertedNumber or x == int(revertedNumber / 10)
    #最后一步 考虑了数的奇偶性

# 执行用时 :92 ms , 在所有 Python 提交中击败了 22.48% 的用户
# 内存消耗 : 11.7 MB , 在所有 Python 提交中击败了 25.12% 的用户

test = Solution().isPalindrome(-10)
print(test)

