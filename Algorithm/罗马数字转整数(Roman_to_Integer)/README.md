# 罗马数字转整数(Roman_to_Integer)
## 简介
* [实践时间(Week 04)](/Weeks/Week_04.md)
* [原题出处(Leetcode)]( https://leetcode-cn.com/problems/roman-to-integer)
## 题目描述  
罗马数字包含以下七种字符: <code>I</code>,<code>V</code>,<code>X</code>,<code>L</code>,<code>C</code>,<code>D</code>,<code>M</code>。
<pre>
<strong>字符</strong>          <strong>数值</strong>
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
</pre>

<P>例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。</P>

<P>通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。
数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：</P>

- I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
- X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
- C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

<P>给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。</P>

## 示例  
<pre>
输入: "III"      
输出: 3
<br>
输入: "IV"
输出: 4 
<br>
输入: "IX"
输出: 9 
<br>
输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3. 
<br>
输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
</pre>

## 解题思路
- 题目分析：
<pre>
1. 正常情况：
1.1 罗马数字对应整数：对应整数为每个罗马数字值相加
1.2 罗马数字位置：大数左小数右

2. 特殊情况
2.1 特定罗马数字对应情况：4,9 罗马数字位置是小数左大数右，两数为一值
2.2 输入的罗马数字只有一位时
</pre>

- 题目设想：
<pre>
1. 首先不考虑特殊情况
2. 再加上特殊情况 另做处理
2.1 添加一个暂时数组，保存上一个字符（i-1）用于比较
2.2 在此需另考虑一个情况（单个字符时，无法比较，(i-1)超出范围另做处理）
2.3 若上一个字符值小于目前值 则说明可能出现特殊情况
2.4 题目外：还需考虑是否符合特殊情况的排列，不符合常规的剔除
</pre>

- 期望目标：
<pre>代码简洁 效率高</pre>

## 实现代码
```python
# 按题目设想：当前字符与上一个字符进行比较，若大于上个字符，则先判断两者一起是否满足特殊情况中的排列组合方式。
#            满足条件后，对该组合对应值进行处理。
# 对只有一个字符的情况，进行单独处理，直接加值
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = []
        result = 0
        Roman_special_dict = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']}
        Roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i, c in enumerate(s):
            if c in Roman_dict and i > 0:
                if Roman_dict[temp[i - 1]] < Roman_dict[c]:
                    """含特殊罗马字符"""
                    if temp[i - 1] in Roman_special_dict and c in Roman_special_dict[temp[i - 1]]:
                        result += Roman_dict[c] - Roman_dict[temp[i - 1]] * 2
                    else:
                        return None
                else:
                    """无特殊罗马字符"""
                    result += Roman_dict[c]

            if c in Roman_dict and i == 0:
                """只有一个字符"""
                result += Roman_dict[c]

            temp.append(c)

        if result <= 3999 and result >= 1:
            return result

# 执行用时 : 36 ms, 在所有 Python 提交中击败了97.56%的用户
# 内存消耗 :11.7 MB, 在所有 Python 提交中击败了28.35% 的用户
```
## 参考代码

[源码出处](https://leetcode-cn.com/problems/roman-to-integer/solution/2-xing-python-on-by-knifezhu/ "罗马数字转整数(Roman_to_Integer)")

```python
#第一种 将特殊情况一起放进字典，两两配对进行匹配  最简洁写法！
# 思路：将所有情况的罗马字符加入字典中，依次遍历字符串的字符，第一次只取一个，从第二次开始，将上一个字符与当前字符结合，看是否在字典中有匹配的：
#     没有，则说明是正常情况，当前字符不再特殊情况中，直接将其值存入结果中。
#     有，则加上字典内俩位字符对应值。
# 特殊情况两个字符代表一个值时取值修改：因为第一个字符的值不应被存入结果中，但被误存了。
# 故在字典中，特殊情况的两个字符的正常结果需要减去第一个字符的值。
#   例如：IVIV 当遍历到第三个I,VI不在字典内，被存入I值，但I为特殊情况，不存在此搭配，故IV原值减去I的值

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))
# 执行用时 :64 ms , 在所有 Python 提交中击败了94.4%的用户
# 内存消耗 :14 MB, 在所有 Python 提交中击败了5.25%的用户
```

***技巧！！！：用max()排除只有一个字符时，索引 i-1 超出范围的情况***

[源码出处](https://leetcode-cn.com/problems/roman-to-integer/solution/python3-bao-li-jie-fa-by-kanomei/ "罗马数字转整数(Roman_to_Integer)")

```python
# 第二种 逐位比较，当前值小于后一位值，则做减法。反之，加法
# 但在处理最后一位时，该代码是单独进行的处理。直接加上最后一位代表的值。
class Solution:
    def romanToInt(self, s: str) -> int:
        roma_nums = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        num = 0
        for i in range(len(s)-1):
            if roma_nums[s[i]]>=roma_nums[s[i+1]]:
                num += roma_nums[s[i]]
            else:
                num -= roma_nums[s[i]]
        last_num = s[len(s)-1]
        num = num + roma_nums[last_num]
        return num
```
<P>该源码可以在处理最后一位上进行优化。利用第一种里的技巧，用max()或min()函数进行范围的限制。或第三种方法的优化，索引倒序。</P>

[源码出处](https://leetcode-cn.com/problems/roman-to-integer/solution/python3-bao-li-jie-fa-by-kanomei/ "罗马数字转整数(Roman_to_Integer)")

```python
# 第二种 逐位比较，当前值小于后一位值，则做减法。反之，加法
# 但在处理最后一位时，该代码是单独进行的处理。直接加上最后一位代表的值。
class Solution:
    def romanToInt(self, s: str) -> int:
        roma_nums = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        num = 0
        for i in range(len(s)-1):
            if roma_nums[s[i]]>=roma_nums[s[i+1]]:
                num += roma_nums[s[i]]
            else:
                num -= roma_nums[s[i]]
        last_num = s[len(s)-1]
        num = num + roma_nums[last_num]
        return num
```
<P>该源码可以在处理最后一位上进行优化。利用第一种里的技巧，用max()或min()函数进行范围的限制。或第三种方法的优化。</P>

[源码出处(作者：左手竖琴)](https://leetcode-cn.com/problems/roman-to-integer/comments/ "罗马数字转整数(Roman_to_Integer)")

```python
# 第三种 可视为第二种的优化 利用if-else处理最后一位
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans=0
        for i in range(len(s)):
            if i<len(s)-1 and a[s[i]]<a[s[i+1]]:
                ans-=a[s[i]]
            else:
                ans+=a[s[i]]
        return ans
```

[源码出处(执行用时为 20 ms 的范例)](https://leetcode-cn.com/problems/roman-to-integer/submissions/ "罗马数字转整数(Roman_to_Integer)")

```python
# 第四种 倒序索引字符  利用一个中间变量，从右往左比较
class Solution(object):
    def romanToInt(self, s):
        roman_id = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        c = 0;
        num = 0;
        for i in range(len(s)-1,-1,-1):
            j = roman_id[s[i]]
            # 如果当前字符小于上次迭代的字符，那么属于特殊请求（e.g.,CD,IV..）
            if j < c:
                num -= j
            # 否则直接相加
            if j >= c:
                num += j
            c = j
        return num
```

## 总结
### 过程中出现的问题：
1. 把一些题目中未说明的点考虑进去，导致代码冗长。而参考代码基本没有考虑是否符合现实规则。
2. 对于代码的整体思路在初期还是不太能快速理清
3. 在特殊情况处理时，解决效率不高

### 出现的新思路：
1. 将特殊情况写入一个字典
2. 用max()，min()进行索引限制
3. 用if （索引长度-1）-else进行索引特殊情况处理

### 优化改善代码
在参考了第一种参考代码用max()限制索引的技巧后，修改了第二种参考代码
用min()函数 从左到右进行判断，到最后一个直接索引到自身。
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roma_nums = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        num = 0
        s_lenth=len(s)
        for i in range(s_lenth):
            if roma_nums[s[i]]>=roma_nums[s[min(i+1,s_lenth-1)]]:
                num += roma_nums[s[i]]
            else:
                num -= roma_nums[s[i]]
        return num
```
