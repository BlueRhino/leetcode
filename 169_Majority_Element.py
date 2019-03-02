from typing import List


class Solution:
    @staticmethod
    def majority_element(nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        seed = nums[0]
        count = 1
        for tmp in nums[1:]:
            if tmp == seed:
                count += 1
            else:
                count -= 1
                if count == 0:
                    seed = tmp
                    count = 1
        return seed


if __name__ == '__main__':
    Solution.majority_element([2, 2, 1, 1, 1, 2, 2])
