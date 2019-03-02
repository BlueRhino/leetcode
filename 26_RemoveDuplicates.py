from typing import List


class Solution:
    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return length
        i, j = 0, 1
        while i < length and j < length:
            a = nums[i]
            while j < length:
                if nums[j] != a:
                    nums[i + 1] = nums[j]
                    break
                else:
                    j += 1
            i += 1
        return i


if __name__ == '__main__':
    Solution.remove_duplicates([1, 1, 2])
