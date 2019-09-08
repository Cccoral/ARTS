# 整数反转(Reverse Integer)
## 简介
* [实践时间(Week 02)](/Weeks/Week_02.md)
* [原题出处(Leetcode)]( https://leetcode-cn.com/problems/reverse-integer)
## 题目描述  
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
<br>**注意**
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
## 示例  
>输入: 123      
输出: 321<br>     
输入: -123<br>
输出: -321<br>
<br>输入: 120<br>
输出: 21<br>
## 解题思路
- 题目分析：
1. 32位有符号的整数，负整数要注意保留负号  
2. 正整数 <2^31-1，考虑正整数后有0的情况
3. 负整数 >-2^31，考虑负整数后有0的情况
4. 整数等于0的情况<br>
- 题目设想：将整数转换成字符串，再判断是否满足各个条件，创建空字符串用于存储满足条的字符串，最终将整个字符串转换回整数。
- 期望目标：以尽可能少的代码完成 
## 实现代码
```python
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
# 执行用时 :52 ms, 在所有 Python 提交中击败了5.97%的用户
# 内存消耗 :11.6 MB, 在所有 Python 提交中击败了34.10%的用户
# 效率实在是太低了，太菜了，条件判断太多，太冗余
```
## 参考代码
[源码出处]( https://leetcode-cn.com/problems/reverse-integer/solution/zheng-shu-fan-zhuan-python-by-fei-ben-de-cai-zhu-u/ "整数反转(Reverse Integer)")
```python
# 解法一：还是将数字转换为字符
# 本题的思路就是先判断给定整数x的正负情况，把符号首先给提取出来
# 然后将abs(x)变成字符串，接着将字符串反转，最后恢复成整数

class Solution(object):
        def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
       flag = 1 if x >= 0 else -1
        abs_x = abs(x)
        # 将abs(x)变成字符串
        x_str = str(abs_x)
        # 将字符串x_str反转
        reverse_x_str = x_str[::-1]
        # 最后恢复成整数
        reverse_x_int = int(reverse_x_str) * flag
        if -2 ** 31 <= reverse_x_int <= 2**31 - 1:
            return reverse_x_int
        else:
            return 0


if __name__ == "__main__":
    x = 231
    reverse_x = Solution().reverse(x)
print(reverse_x)
```
[源码出处]( https://leetcode-cn.com/problems/reverse-integer/solution/reverse-integer-by-jin407891080/ "整数反转(Reverse Integer)")
```python
# 解法二：数字直接进行算术运算 不需要转换
#对当前数取对 10 的余数，再一项项填入res尾部，即可完成 intint 翻转。
# Python的坑： 由于Python的 // 操作是向下取整，导致正负数取余 % 操作结果不一致，因此需要将原数字转为正数操作。
class Solution:
    def reverse(self, x: int) -> int:
        y, res = abs(x), 0
        of = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            res = res * 10 + y % 10
            if res > of: return 0
            y //= 10
        return res if x > 0 else -res 
```
[源码出处]( https://leetcode-cn.com/problems/reverse-integer/solution/hua-jie-suan-fa-7-zheng-shu-fan-zhuan-by-guanpengc/  "整数反转(Reverse Integer)")
```python
# 解法三： 数字直接进行算术运算 不需要转换
#由于字符串转换的效率较低且使用较多库函数，所以解题方案不考虑该方法，而是通过数学#计算来解决。通过循环将数字x的每一位拆开，在计算新值时每一步都判断是否溢出。
#源码为C++，自行修改成python格式
class Solution :
    def reverse(self,x):
        rev = 0
        while(x != 0):
            pop = int(x % 10)
            x = int(x / 10)
            if(rev > int((2**31-1) / 10 )or (rev == int((2**31-1)/ 10) and pop > int((2**31-1) % 10))):
                rev = 0
                break
            elif(rev < int((-2**31) / 10) or (rev == int((-2**31)/ 10) and x < int((-2**31) % 10))):
                rev = 0
                break
            # if rev > int((2**31-1) / 10 ):
            #     rev = 0
            #     break
            # elif rev <int( (-2**31) / 10 ):
            #     rev = 0
            #     break
            rev = rev * 10 + pop
        return rev
```
## 总结
### 过程中出现的问题：
1.	总把问题解想复杂，第一次设置了两个for循环，第一次用于无论正负数均反转所有字符，第二次对反转后的字符进行满足数值条件的判断。效率极低
2.	第二次只设置一个for循环，对正负数分别进行处理，在读取每个数的字符的同时进行反转，设置条件还是太多，效率低。
3.	没有考虑到可以先将负数进行绝对化处理，简化步骤
### 出现的新思路：
参考他人代码后，认为还是直接对数进行算术运算最为简洁，高效。<br>
若一定要转换到字符串形式实现，可以参考解法一，设置一个标志符，及绝对化负数，统一成整数进行反转处理，再恢复。<br>
算术运算的话，主要三步，第一取出尾数，第二原数去尾，第三尾数进行运算实现反转<br>
个人认为参考代码中的解法二目前最佳
### 优化改善代码
