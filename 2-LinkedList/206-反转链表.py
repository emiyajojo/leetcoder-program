from typing import Optional
from LinkedNode import *
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 共需要3个指针，其中一个是暂时指针
        # 不需要虚拟头节点
        pointer=head
        pre=None
        while pointer:
            temp=pointer.next
            pointer.next=pre
            pre=pointer
            pointer=temp
        # 最后返回pre，因为退出while的时候，pointer已经是空
        return pre