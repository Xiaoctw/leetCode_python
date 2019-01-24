class Solution(object):
    def twoSum(self, nums, target):
        """
        这个需要注意字典获取对应的值的两种方法，get方法如果没有对应的键值时会返回none，而用中括号会抛出异常
        而为字典中特定键赋值时必须用中括号
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicts = {}
        for k, v in enumerate(nums):
            if target - v in dicts:
                return [dicts.get(target - v), k]
            dicts[v] = k
