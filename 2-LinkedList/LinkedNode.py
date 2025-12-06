class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    @staticmethod
    def makeLinkedList(arr)-> ListNode:
        if not arr:
            return None
        head=ListNode(arr[0])
        pre=head
        for val in arr[1:]:
            newNode=ListNode(val)
            pre.next=newNode
            pre=pre.next
            
        return head
    
    @staticmethod
    def printLinked(head:ListNode):
        while head:
            if head.next:
                print(str(head.val)+" --> ",end="")
            else:
                print(str(head.val))
            head=head.next
        
        