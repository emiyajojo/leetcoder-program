"""
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
示例 1：

输入：head = [1,2,3,4]
输出：[2,1,4,3]

示例 2：

输入：head = []
输出：[]

示例 3：

输入：head = [1]
输出：[1]

 

提示：

    链表中节点的数目在范围 [0, 100] 内
    0 <= Node.val <= 100

"""
from LinkedNode import *
from typing import Optional
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        记住1-->2-->3这个模型
        最后返回头节点,但不是原来的head, head已经是第二个节点了,需要以虚拟头节点为主
        """
        fake_head=pt=ListNode(0,head)
        
        while pt.next and pt.next.next:
           temp=pt.next 
           pt.next=temp.next 
           temp.next=temp.next.next
           pt.next.next=temp
           pt=temp
        
        return fake_head.next
         
            

