"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.


Example 1)
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""
def set(head) -> bool:
    """
    set 활용
    """
    node_set = set()

    while head:
        if head in node_set:
            return True
        node_set.add(head)
        head = head.next

    return False
            
def two_pointer(head) -> bool:
    """
    slow, fast 두 개의 포인터 활용
    """
    if head is None:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False
        
        slow = slow.next
        fast = fast.next.next
    return True

head = []