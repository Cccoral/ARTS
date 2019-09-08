# 回文数(palindrome_number)
## 简介
* [实践时间(Week 03)](/Weeks/Week_03.md)
* [原题出处(Leetcode)]( https://leetcode-cn.com/problems/palindrome-number)
## 题目描述  
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
## 示例  
>输入: 12      
输出: true<br>     
输入: -121<br>
输出: false<br>
<br>输入: 10<br>
输出: false <br>
## 解题思路
- 题目分析：
1. 输入0，应返回True
2. 输入10，应返回False<br>
- 题目设想：第一想法是将数字转换成列表，利用其内置的reverse()函数进行倒序比较，也有考虑直接算术运算比较，但觉得应该没有转换来的简洁和快。
- 期望目标：代码简洁 效率高
## 实现代码
```python
# 第一种 转换成列表 利用reverse()倒序
class Solution(object):
    def isPalindrome(self, x):
        y = list(str(x))
        x = list(str(x))
        y.reverse()
        if y == x:
            return True
        else:
            return False
# 执行用时 : 44 ms, 在所有 Python 提交中击败了97.69%的用户
# 内存消耗 :11.7 MB, 在所有 Python 提交中击败了29.53% 的用户
```
```python
# 第二种 转换成字符串 利用切片倒序
class Solution(object):
    def isPalindrome(self, x):
         y=str(x)
         x=str(x)
         y = y[::-1]
         if y == x:
             return True
         else:
             return False
# 执行用时 :76 ms , 在所有 Python 提交中击败了41.39%的用户
# 内存消耗 :11.6 MB, 在所有 Python 提交中击败了33.35%的用户
```
## 参考代码
[源码出处](https://leetcode-cn.com/problems/palindrome-number/solution/hui-wen-shu-by-leetcode/ "回文数(palindrome number)")
```python
# 解法一：还是将数字转换为字符
# 本题的思路：直接数值运算，取一半位数与另一半做比较
# 如何知道反转数字的位数已经达到原始数字位数的一半？
# 将原始数字除以 10，然后给反转后的数字乘上 10，当原始数字小于反转后的数字时，意味着已经处理了一半位数的数字。

class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x = int(x / 10)
        return x == revertedNumber or x == int(revertedNumber / 10)
```
## 总结
### 过程中出现的问题：
1.  这次问题没有想复杂，但发现每次leetcode运行后的时间都不一致，相差可达十几毫秒，目前让我无法判断谁更好
2.	python的内置函数reverse()是用c语言编写，若要查看具体步骤，需要找python开源里的c文件，目前我还没有找到
3.  切片的使用还可以探索
### 出现的新思路：
在参考了其他人的思路后，觉得都不太简洁。可能跟语言差异有关
### 优化改善代码
无
