from typing import List


class Solution:
    res = []

    @staticmethod
    def partition(s: str) -> List[List[str]]:
        Solution.get_palindrome(s, 0, [])
        return Solution.res

    @staticmethod
    def get_palindrome(s: str, start: int, current_list: list):
        if len(s) == start:
            Solution.res.append(current_list)

        for i in range(start, len(s)):
            if s[start:i + 1] == s[start:i + 1][::-1]:
                current_list.append(s[start:i + 1])
                Solution.get_palindrome(s, i + 1, current_list)


if __name__ == '__main__':
    print(Solution.partition('cdd'))
