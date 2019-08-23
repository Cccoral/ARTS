#第一次 嵌套循环
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
print(Solution().twoSum([4,2,2,3,4,3],6))

# 第二次 修改代码  哈希字典
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
print(Solution().twoSum([4,2,2,3,4,3],6))

#参考代码
# 作者：smallhi
# 链接：https://leetcode-cn.com/problems/two-sum/solution/python3-san-chong-jie-fa-by-smallhi/
# 来源：力扣（LeetCode）

# 解法一 暴力循环：
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
def tow_sum_with_dict2(nums: List[int], target: int) -> List[int]:
    _dict = {}
    for i, m in enumerate(nums):
        if _dict.get(target - m) is not None:
            return [i, _dict.get(target - m)]
        _dict[m] = i
# 时间复杂度为O（n）
# 空间复杂度为O（n）
# 46ms

