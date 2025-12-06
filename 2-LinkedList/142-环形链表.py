from typing import *
from LinkedNode import *
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        how to find the 1st node of the ring?
        fast: 2 steps each time
        slow: 1 step
        x=distance from first node of the whole link to the first node of ring(Ring-head)
        y=Ring head to the node where slow and fast meets
        z=length of Ring - y
        
        distance of slow has walked = x+y
        a truth: slow will definitely meet fast in his own 1st ring
        fast: total distance = x+(y+z)*n, n is the rings number
        2(x+y) = x+(y+z)*n+y
        x = (n-1)y+n*z
        x = (n-1)(y+z)+z
        ignore (n-1)(y+z), the rings number, x=z
        
        so we need the node where they meet
        """
        slow=fast=head
        node=head
        new_node=ListNode(node,None)
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            
            if fast==slow:
                new_node=fast
                break
        
        while new_node!=node:
            node=node.next
            new_node=new_node.next
        
        return node
    
                
                
            
        
        