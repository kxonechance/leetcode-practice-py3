#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        fast = head
        slow = head
        prev = dummy

        for i in range(n):
            fast = fast.next
        
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next

        prev.next = slow.next

        return dummy.next

# @lc code=end

