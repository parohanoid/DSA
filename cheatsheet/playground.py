class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode) -> ListNode:
    c = head
    cd = c
    cd.next = None
    cp = cd
    c = c.next
    while c:
        cd = c
        cd.next = cp
        cp = cd
        c = c.next
    
    cd.next = cp
    return cd

# debug your code below
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
reversed_head = reverse_list(head)
print(reversed_head.val)
print(reversed_head.next.val)