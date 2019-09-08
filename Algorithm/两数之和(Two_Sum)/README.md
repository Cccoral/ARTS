# 两数之和(Two Sum)
## 简介
* [实践时间(Week 01)](/Weeks/Week_01.md)
* [原题出处(Leetcode)](https://leetcode-cn.com/problems/two-sum)
## 题目描述  
给定一个整数数组 **nums** 和一个目标值 **target**，请你在该数组中找出和为目标值的那**两个**整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
## 示例  
输入条件 nums = [2, 7, 11, 15], target = 9  
解决过程 nums[0] + nums[1] = 2 + 7 = 9  
输出结果 [0, 1]
## 解题思路
- 题目分析：1.只找出两个整数之和   2.不能重复利用同样的元素
- 题目设想：遍历整个列表，利用目标值减去当前值得到对应值。再搜索对应值是否存在于列表中，若存在，则输出两者的索引值
- 期望目标：在完成题目要求上，若存在多个结果，都能输出  
## 实现代码
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        results = []   
        for i in range(len(nums)):
            value = target - nums[i]
            for k in range(len(nums[i + 1:])):
                index = i + 1 + k
                if nums[index] == value :
                    if i not in results:
                        results.append(i)
                        results.append(index)
                    else:
                        break   
        return (results)
# 执行用时 :5680ms, 在所有 Python 提交中击败了11.36%的用户
```
## 参考代码
[源码出处](https://leetcode-cn.com/problems/two-sum/solution/python3-san-chong-jie-fa-by-smallhi/ "两数之和（two_sum）")
```python
# 解法一：暴力破解
def two_sum(nums: List[int], target: int) -> List[int]:
    size = len(nums)
    for i, m in enumerate(nums):
        j = i + 1
        while j < size:
            if target == (m + nums[j]):
                return [i, j]
            else:
                # print(i, j, m + _n, " didn't match!")
                j += 1
# 时间复杂度为 O（n^2）
# 空间复杂度为O(1)
# 60ms

# 解法二：字典模拟Hash 
# 从前往后.先将列表遍历一遍,值和索引值存入字典, 再从头遍历是否有符合条件的值,输出结果
def tow_sum_with_dict(nums: List[int], target: int) -> List[int]:
    _dict = {}
    for i, m in enumerate(nums):
        _dict[m] = i

    for i, m in enumerate(nums):
        j = _dict.get(target - m)
        if j is not None and i != j:
            return [i, j]
# 时间复杂度为O（n）
# 空间复杂度为O（n）
# 52ms

# 解法三：一遍字典模拟Hash  
# 从后往前.在遍历列表，存入字典过程中，从字典的当前元素向前进行匹配是否有对应元素,一次遍历完则匹配完成
def tow_sum_with_dict2(nums: List[int], target: int) -> List[int]:
    _dict = {}
    for i, m in enumerate(nums):
        if _dict.get(target - m) is not None:
            return [i, _dict.get(target - m)]
        _dict[m] = i
# 时间复杂度为O（n）
# 空间复杂度为O（n）
# 46ms
```
## 总结
### 过程中出现的问题：
  1. 搜索对应值应在未遍历的元素内查找，不应从头遍历，避免出现重复结果
  2. 考虑情况不够详细。例：同一元素出现多组匹配结果的情况
  3. 时间复杂度和空间复杂度没有考虑，对两者的了解也不够
### 出现的新思路：
  在参考他人代码后，知道了哈希映射的概念。在python中可以用字典进行模拟。但仍对哈希还不够了解。
  对于本题的思考一直都停留在对数组进行从前往后完整的遍历，未考虑过可以利用字典，进行从后往前的匹配。
  个人认为参考代码中的解法三目前最佳
### 优化改善代码
```python
#基于解法三，更换了思路重写代码。解法三只考虑输出一组结果，未达到我的期望。
#因此我改善的代码是基于我的期望目标：输出多个结果 进行调整的
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        results=[]
        dic = {}
        for index,num in enumerate(nums):
            value=target-num
            if value in dic :
                if dic.get(value) not in results:
                    results.append(index)
                    results.append(dic.get(value))
            dic[num]=index
        return results
        
# 执行用时 :52 ms, 在所有 Python 提交中击败了75.59%的用户
# 内存消耗 :13.2 MB, 在所有 Python 提交中击败了9.50%的用户


   
