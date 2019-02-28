from typing import List


class Solution:
    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        length = len(nums)
        i, j = 0, 1
        count = 0
        while i < length:
            a = nums[i]
            while j < length:
                if nums[j] != a:
                    count += j - i
                    break
                else:
                    j += 1
            nums[i+1:] = nums[j:]
            i += 1
        return length - count


if __name__ == '__main__':
    Solution.remove_duplicates([1, 1, 2])
