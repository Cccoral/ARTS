# 最长公共前缀(Longest_Common_Prefix)
## 简介
* [实践时间(Week 05)](/Weeks/Week_05.md)
* [原题出处(Leetcode)](https://leetcode-cn.com/problems/longest-common-prefix/)
## 题目描述  
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串<code>""</code>。

## 示例  
<pre>
输入: ["flower","flow","flight"]
输出: "fl"

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
</pre>

## 解题思路
- 题目分析：
<pre>
1.有前缀，输出前缀
2.均无前缀，输出空
</pre>

- 题目设想：
<pre>
因为找出前缀，首先想到的则是将每个单词的字母进行逐位对比。
考虑停止条件：以最小长度的单词为标准。
第一步：找出最小长度的单词，及其长度
第二步：在遍历最小长度次数的循环中，一次对每个单词相应位进行对比判断
一旦出现某处不一致，则返回结果

注意：当输入为空时，输出也是""
感觉自己思考的有点复杂，代码会写的冗长，繁杂
</pre>

- 期望目标：
<pre>学习他人的思路，对自己的思路进行改进</pre>

## 实现代码
```python
# 按题目设想
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if strs:
            min_length=len(strs[0])
        else:
            return ''

        for i,s in enumerate(strs):
            if len(s)<=min_length:
                min_s=s
                min_length = len(s)

        result=''
        for c in range(len(min_s)):
            for i,v in enumerate(strs):

                if min_s[c]==v[c] and i==len(strs)-1:
                    result+=min_s[c]
                elif min_s[c] != v[c] and result!='':
                    return result
                elif min_s[c] != v[c] and result=='':
                    return ""
# 执行用时 : 32 ms, 在所有 Python 提交中击败了39.44%的用户
# 内存消耗 :11.7 MB, 在所有 Python 提交中击败了34.38% 的用户
```
## 参考代码

[源码出处](https://leetcode-cn.com/problems/longest-common-prefix/solution/2-xing-python-by-knifezhu-2/ "最长公共前缀(Longest_Common_Prefix)")

```python
#第一种 最简洁写法！充分利用了python的内置函数zip()和set() 
# 思路：利用zip（*）解压形式，将每个单词对应位置的字母分别划分为一组，再利用set()特点，除重后返回满足条件的bool数组
# 再将bool数组结果与某单词做匹配，输出结果。
class Solution(object):
    def longestCommonPrefix(self, strs):
        re=[len(set(i))==1 for i in zip(*strs)]
        return(strs[0][:re.index(False)] if strs else '')
```

***技巧！！！：巧用zip（）连接需要分组的字符，set()除重***

[源码出处](https://leetcode-cn.com/problems/longest-common-prefix/solution/duo-chong-si-lu-qiu-jie-by-powcai-2/ "最长公共前缀(Longest_Common_Prefix)")

```python
# 第二种 
#思路:以第一个字符串作为参考，依次与之后每一个字符串做对比匹配。匹配不成功就自动减位，重新比较。将每次匹配到的结果作为与下一个字符串匹配#的参考
#字符串 find():用作匹配 -1 不匹配 0 匹配
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        res = strs[0]
        
        i = 1
        while i < len(strs):
            while strs[i].find(res) != 0:
                res = res[0:len(res) - 1]
            i += 1
        return res
```
***技巧！！！：巧用find（）进行匹配，同时利用切片进行匹配字符串的减位***

[源码出处](https://leetcode-cn.com/problems/longest-common-prefix/solution/duo-chong-si-lu-qiu-jie-by-powcai-2/ "最长公共前缀(Longest_Common_Prefix)")

```python
# 第三种
# 思路:首先，先将字符串进行排序，利用其逐位比较的特点，可以将有相同前缀的单词聚集起来，再依次排序
# 最后只比较第一个和最后一个单词的每一位确定前缀
class Solution:
    def longestCommonPrefix(self, s):
        if not s:
            return ""
        s.sort()
        
        n = len(s)
        a = s[0]
        b = s[n-1]
        
        res = ""
        for i in range(len(a)):
            if i < len(b) and a[i] == b[i]:
                res += a[i]
            else:
                break
        return res
```
<P>巧妙之处：利用排序的特点，且在循环的时候以第一个单词长度循环，再以最后一个单词长度做判断处理</P>

## 总结
### 过程中出现的问题：
1. 思考问题还是过于复杂
2. 对于python的函数使用还是不太熟悉，需要多多练习巩固

### 出现的新思路：
在参考代码中已经囊括差不多了，暂时未想到其他新的方法

### 优化改善代码
无
