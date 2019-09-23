# 题目说明 链接：https://leetcode-cn.com/problems/roman-to-integer
# # 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
# # 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
# #
# # I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# # X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# # C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# # 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

# 题目分析
# # 通常情况
# # 1. 罗马数字对应整数 组合重复其值 相加
# # 2. 罗马数字位置 大数小数
#
# # 特殊情况
# # 1. 4,9 罗马数字位置 小数大数  特定罗马数字对应情况
# # 2. 只输入一个罗马数字

# 思路
# # 1.第一步 首先不考虑特殊情况
# # 2.第二 加上特殊情况 另做处理
# # 2.1 添加一个暂时数组 保存上一个字符用于比较
# # 2.2 在此需另考虑一个情况（单个字符时，无法比较，另做处理）
# # 2.3 若上一个字符值小于目前值 则说明可能出现特殊情况
# # 2.4 还需要考虑是否符合特殊情况的排列  不符合剔除

#自行编写
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

#第一种
#  思路：将所有情况的罗马字符加入字典中，依次遍历字符串的字符，第一次只取一个，从第二次开始，将上一个字符与当前字符结合，看是否在字典中有匹配的，没有则说明是正常情况，当前字符不再特殊情况中，直接将其值存入结果中，若有，则加上字典内俩位字符对应值
# 特殊情况两个字符代表一个值时取值修改：因为第一个字符的值不应被存入结果中，但被误存了。故在字典中，特殊情况的两个字符的正常结果需要减去第一个字符的值
# IVIV 当遍历到第三个I,VI不在字典内，被存入I值，但I为特殊情况，不存在此搭配，故IV原值减去I的值
#技巧：用max()排除第一个数i-1变成-1的情况

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))
        # d.get(s[max(i-1,0):i+1],d[n])  获取两个连续字符 查看是否存在于字典，不存在则赋值

# 第二种
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
# 第三种
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

# 第四种
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

# 修改第二种代码
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

s = Solution()
print(s.romanToInt('VIV'))