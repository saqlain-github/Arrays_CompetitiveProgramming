#Naive Approach O(n) O(n)
def detectCycle(head):
    myset = set()
    current = head
    while current:
        if current not in myset:
            myset.add(current)
        else: #detect cycle
            return False
        current = current.next
        
    return True

#o(n) O(1)
def detectCycle_FastandSlow(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False