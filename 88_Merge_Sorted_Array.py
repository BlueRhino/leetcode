from typing import List


class Solution:
    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        由于nums1长度已经预留，直接使用从后往前的比较，最后处理剩余元素即可
        """
        i, j = m - 1, n - 1
        current_index = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[current_index] = nums1[i]
                nums1[i] = 0
                i -= 1
            else:
                nums1[current_index] = nums2[j]
                j -= 1
            current_index -= 1
        if j >= 0:
            nums1[0:current_index + 1] = nums2[0:j + 1]


if __name__ == '__main__':
    nums1s = [0]
    ms = 0
    nums2s = [1]
    ns = 1
    Solution.merge(nums1s, ms, nums2s, ns)
    print(nums1s)
