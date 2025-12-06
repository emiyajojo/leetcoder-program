"""
你可以选择使用单链表或者双链表，设计并实现自己的链表。

单链表中的节点应该具备两个属性：val 和 next 。val 是当前节点的值，next 是指向下一个节点的指针/引用。

如果是双向链表，则还需要属性 prev 以指示链表中的上一个节点。假设链表中的所有节点下标从 0 开始。

实现 MyLinkedList 类：

    MyLinkedList() 初始化 MyLinkedList 对象。
    int get(int index) 获取链表中下标为 index 的节点的值。如果下标无效，则返回 -1 。
    void addAtHead(int val) 将一个值为 val 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
    void addAtTail(int val) 将一个值为 val 的节点追加到链表中作为链表的最后一个元素。
    void addAtIndex(int index, int val) 将一个值为 val 的节点插入到链表中下标为 index 的节点之前。如果 index 等于链表的长度，那么该节点会被追加到链表的末尾。如果 index 比长度更大，该节点将 不会插入 到链表中。
    void deleteAtIndex(int index) 如果下标有效，则删除链表中下标为 index 的节点。
"""
from LinkedNode import *
class MyLinkedList:
    """
    需要有一个类属性记录链表长度
    初始化需要
    """
    def __init__(self):
       self.new_head=ListNode()
       self.len=0 

    def get(self, index: int) -> int:
        if index >self.len-1 or index<0:
            return -1
        # 前面的边界判断已经包含了链表只有一个虚拟头结点的情况
        # 这里，当index==0的时候，取第一个节点值，因此pointer先初始化为new_head.next
        # 在下面的for循环中，若index==0, pointer不需要进入for循环
        # 若index>0，pointer则以此类推
        pointer=self.new_head.next
        for i in range(index):
            pointer=pointer.next
        return pointer.val

    def addAtHead(self, val: int) -> None:
        new_Node=ListNode(val,self.new_head.next)
        self.new_head.next=new_Node
        self.len+=1

    def addAtTail(self, val: int) -> None:
        # 这里需要pointer为非空，因此pointer指向虚拟头节点而不是头节点的下一个节点
        pointer=self.new_head
        while pointer.next:
            pointer=pointer.next
        # 注意推出while的时候pointer.next已经是None,pointer一定是最后一个节点
        pointer.next=ListNode(val)
        self.len+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        # 这里边界条件判断，注意别把index==self.len情况给包含进去，index==self.len在后面直接用addAtTail处理
        if index<0 or index>self.len:
            return
        if index==self.len:
            self.addAtTail(val)
            return
        pointer=self.new_head
        # pointer以及index的对应关系?
        # pointer就在index前
    
        for i in range(index):
            pointer=pointer.next
        pointer.next=ListNode(val,pointer.next)
        self.len+=1
        

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>self.len-1:
            return
        pointer=self.new_head
        for i in range(index):
            pointer=pointer.next
        # after for, is it possible that pointer is None?
        # not possible
        # pointer will stop before index, just like addAtIndex
        # pointer won't arrive the last node
        pointer.next=pointer.next.next
        self.len-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)