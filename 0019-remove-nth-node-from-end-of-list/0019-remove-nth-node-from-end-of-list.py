# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0,head)
        curr=head
        prev=dummyNode

        for _ in range(n):
            curr=curr.next
        
        while(curr):
            curr=curr.next
            prev=prev.next
        
        prev.next = prev.next.next
        return dummyNode.next