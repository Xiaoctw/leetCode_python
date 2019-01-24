# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = b = 0
        carry = 0
        while l1:
            a += l1.val * 10 ** carry
            carry += 1
            l1 = l1.next
        carry = 0
        while l2:
            b += l2.val * 10 ** carry
            carry += 1
            l2 = l2.next
        ret = a + b
        h = m = ListNode(0)
        if not ret:
            return h
        while ret:
            m.next = ListNode(ret % 10)
            ret /= 10
            m = m.next
        return h.next

    def addTwoNumbers(selfl1, l1, l2):
        """
         :type l1: ListNode
        :type l2: ListNode
         :rtype: ListNode
               """
        carry = 0  # 表示进位
        head = None
        tem = None
        while (l1 or l2 or carry):
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            node = ListNode((val1 + val2 + carry) % 10)
            if not head:
                head = node
                tem = head
            else:
                tem.next = node
                tem = node
            carry = (val1 + val2 + carry) // 10
            # l1=l1.next
            # l2=l2.next
        return head
