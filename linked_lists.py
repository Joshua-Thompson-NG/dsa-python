# LINKED LISTS
# It is built from individual objects called Nodes.

# A Node includes
# Data, Next Pointer, Tail (Optional), and Head

# Types of Linked Lists
# 1. Singly Linked List - Can only travel in one direction
# 2. Doubly Linked List - Can travel in both directions, but it requires more memory
# 3. Circular Linked List - The final next Node points back to the head forming a circle.

# Comparing against Arrays
# 1. Arrays are ordered and fixed in size
# 2. Linked Lists are not ordered and can grow and shrink

# Access - for array it's o(1) for LL it's o(n)
# Insertion/Delete (at the start) - for array it's o(n) for LL it's o(1)
# Insertion/Delete (at the end) - for array it's o(1) for LL it's o(n) unless we use a circular LL then it's o(1)

## BluePrint
# Singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val # Data
        self.next = next # Pointer

head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

head.next = node2
node2.next = node3

# Traverse
curr = head
while curr is not None:
    print(curr.val)
    curr = curr.next

# Dummy Node
def removeElements(head, val):
    # 1. Create a dummy node and point its 'next' to the actual head
    dummy = ListNode(0)
    dummy.next = head

    # 2. Start our pointer AT the dummy node
    curr = dummy

    # 3. Look ahead at the NEXT node
    while curr.next is not None:
        if curr.next.val == val:
            # Skip the target node by routing the pointer around it
            curr.next = curr.next.next
        else:
            # Move forward normally
            curr = curr.next

    # Return the real head of the list, which sits right after the dummy
    return dummy.next


# Fast and Slow Pointers
def middleNode(head):
    # Both start at the beginning
    slow = head
    fast = head

    # Fast checks if it can jump 2 steps safely
    while fast is not None and fast.next is not None:
        slow = slow.next  # Moves 1 step
        fast = fast.next.next  # Moves 2 steps

    # When the loop ends, fast is at the end, so slow is in the middle
    return slow

# In place reversal: reversing a linked list in place
def reverseList(head):
    prev = None  # What the current node will point backward to
    curr = head  # The node we are currently flipping

    while curr is not None:
        # 1. SAVE the rest of the list before we sever the connection
        next_node = curr.next

        # 2. FLIP the arrow to point backward
        curr.next = prev

        # 3. MOVE both pointers one step forward for the next loop
        prev = curr
        curr = next_node

    # When curr falls off the end (becomes None), prev is sitting on the new head
    return prev




