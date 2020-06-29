# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
#  如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
#  您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
#  示例：
#
#  输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#
#  Related Topics 链表 数学


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 简单思路，后续考虑可以在加的时候直接处理进位
# 执行用时：64 ms, 在所有 Python3 提交中击败了96.60%的用户
# 内存消耗：13.8 MB, 在所有 Python3 提交中击败了5.13%的用户
class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_point = l1  # 初始化指针
        l2_point = l2  # 初始化指针
        while l1_point is not None and l2_point is not None:
            val = l1_point.val + l2_point.val
            # 两个列表同时修改
            l1_point.val = val
            l2_point.val = val
            l1_point = l1_point.next
            l2_point = l2_point.next
        # 取长的列表
        res = l1
        if l1_point is None:
            res = l2
        is_carry = 0
        res_point = res  # 初始化指针
        # 处理进位
        while True:
            res_point.val += is_carry
            if res_point.val > 9:
                res_point.val -= 10
                is_carry = 1
            else:
                is_carry = 0
            # 处理最后一个进位
            if res_point.next is None:
                if is_carry:
                    res_point.next = ListNode(1)
                break
            else:
                res_point = res_point.next
        return res


# 转换为整数再转回来，很烂
# 执行用时：80 ms, 在所有 Python3 提交中击败了43.83%的用户
# 内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.13%的用户
class Solution2(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        int1 = int2 = 0
        point1 = l1
        count = 1
        while point1:
            int1 += point1.val * count
            count *= 10
            point1 = point1.next
        count = 1
        point1 = l2
        while point1:
            int2 += point1.val * count
            count *= 10
            point1 = point1.next
        res_int = int1 + int2
        res = ListNode(0)
        if res_int == 0:
            return res
        point1 = res
        while res_int >= 10:
            point1.next = ListNode(res_int % 10)
            res_int = res_int // 10
            point1 = point1.next
        if res_int:
            point1.next = ListNode(res_int)
        return res.next


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    list1 = ListNode(1)
    p = list1
    for i in range(20):
        p.next = ListNode(0)
        p = p.next
    p.next = ListNode(1)
    list2 = ListNode(5)
    list2.next = ListNode(6)
    list2.next.next = ListNode(4)
    res_ = Solution2().addTwoNumbers(list1, list2)
    while res_ is not None:
        print(res_.val)
        res_ = res_.next
