class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        int_max = 2147483647
        int_min = -2147483648
        if x < 0:
            y = -1 * int(str(-x)[::-1])
        else:
            y = int(str(x)[::-1])
        if y > int_max or y < int_min:
            return 0
        return y
