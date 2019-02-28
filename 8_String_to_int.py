class Solution(object):
    @staticmethod
    def my_atoi(ss):
        """
        :type ss: str
        :rtype: int
        """
        int_max = 2147483647
        int_min = -2147483648
        index = 0
        while index < len(ss) and ss[index] == ' ':
            index += 1
        flag = 1
        if index < len(ss) and ss[index] == '-':
            index += 1
            flag = -1
        elif index < len(ss) and ss[index] == '+':
            index += 1
        res = 0
        while index < len(ss):
            if ss[index] < '0' or ss[index] > '9':
                return flag * res
            digit = ord(ss[index]) - ord('0')
            if flag == 1 and res * 10 + digit > int_max:
                return int_max
            if flag == -1 and res * 10 + digit > -int_min:
                return int_min
            res = res * 10 + digit
            index += 1
        return flag * res
