# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
#  示例 1:
#
#  输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
#  示例 2:
#
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
#  示例 3:
#
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#  Related Topics 哈希表 双指针 字符串 Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
# 大道至简的解法，找出所有子串进行判断
# 提交超出时间限制：）
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        all_substring = [s[i:(i + x + 1)] for x in range(len(s)) for i in range(len(s) - x)]
        longest = 0
        for ss in all_substring:
            ok = True
            tmp = set()
            for char in ss:
                if char in tmp:
                    ok = False
                    break
                else:
                    tmp.add(char)
            if ok:
                longest = len(ss) if len(ss) > longest else longest
        return longest


# 尝试简单优化一下
# 执行用时：456 ms, 在所有 Python3 提交中击败了16.12%的用户
# 内存消耗：18.8 MB, 在所有 Python3 提交中击败了5.88%的用户
# 烂爆了
class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        all_res = []
        go_on = True
        while go_on:
            go_on = False
            for i in range(1, len(s)):
                if s[i] in s[0:i]:
                    all_res.append(s[0:i])
                    s = s[s.index(s[i]) + 1:]
                    go_on = True
                    break
        all_res.append(s)
        len_list = [len(x) for x in all_res]
        len_list.sort(reverse=True)
        return len_list[0]


if __name__ == '__main__':
    res = Solution2().lengthOfLongestSubstring('abcabcbb')
    print(res)
