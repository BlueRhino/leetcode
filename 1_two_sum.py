# Given an array of integers, return indices of the two numbers such that they a
# dd up to a specific target.
#
#  You may assume that each input would have exactly one solution, and you may n
# ot use the same element twice.
#
#  Example:
#
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#  Related Topics Array Hash Table


# leetcode submit region begin(Prohibit modification and deletion)
# 遍历模式，简单、性能低
# 执行用时：3176 ms, 在所有 Python 提交中击败了28.52%的用户
# 内存消耗：13.4 MB, 在所有 Python 提交中击败了7.41%的用户
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_ = len(nums)
        for i in range(0, len_ - 1):
            for j in range(i + 1, len_):
                if nums[i] + nums[j] == target:
                    return i, j


# 使用python自带的列表查找
# 执行用时：796 ms, 在所有 Python 提交中击败了44.48%的用户
# 内存消耗：13.4 MB, 在所有 Python 提交中击败了6.17%的用户
# 相对第一种解法，主要减少了执行时间
# TODO：此处可以详细研究python自带的列表查找元素的方式
class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_ = len(nums)
        for i in range(0, len_):
            sub = target - nums[i]
            if sub in nums:
                sub_i = nums.index(sub)
                if sub_i != i:
                    return i, sub_i


# 解法三，对于解法二的简单优化
# 对于已经使用过的元素不会再次使用，已经比对过的元素也不需要再次比对
# 所以可以不断缩短待比较的列表长度
# 执行用时：700 ms, 在所有 Python 提交中击败了50.71%的用户
# 内存消耗：13.4 MB, 在所有 Python 提交中击败了7.41%的用户
# 与解法二没有明显的差别
# TODO：此处可以详细研究切片对于性能的影响
class Solution3(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_ = len(nums)
        for i in range(0, len_ - 1):
            sub = target - nums[i]
            nums_part = nums[i + 1:]  # 只需要比较后面的元素
            if sub in nums_part:
                sub_i = nums_part.index(sub) + i + 1  # 需要加上前面的长度
                return i, sub_i


# 针对解法二和解法三分析，其中最列表查找应该最耗时间
# 使用Map可以优化查找时间
# 执行用时：32 ms, 在所有 Python 提交中击败了87.74%的用户
# 内存消耗：14.1 MB, 在所有 Python 提交中击败了6.17%的用户
# 解法四明显快于以上三个解法
class Solution4(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_ = len(nums)
        map_ = {}
        for i in range(0, len_):
            sub = target - nums[i]
            if sub in map_:
                return i, map_[sub]
            else:
                map_[nums[i]] = i


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution4()
    print(s.twoSum([3, 2, 4], 6))
