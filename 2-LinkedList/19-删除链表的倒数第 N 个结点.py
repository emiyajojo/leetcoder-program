"""给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

 

示例 1：

输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：

输入：head = [1], n = 1
输出：[]

示例 3：

输入：head = [1,2], n = 1
输出：[1]

 

提示：

    链表中结点的数目为 sz
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
"""
from typing import Optional
from LinkedNode import *
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        key idea is to use double pointers, the steps that faster is the n
        pay attention to initialize: fast and slow should point to the sentinel head node
        also notice that fast one should use n+1 loops in 'for', so that slow can delete the target node easily
        """
        senti_head=f=s=ListNode(0,head)
        for _ in range(n+1):
            f=f.next
        # f just traverse to the last node, s will stop before the nth node
        while f:
            f=f.next
            s=s.next
        s.next=s.next.next
        return senti_head
        
        
        
        
        
