# Stacks and Queues

# They are sequential data structures that control exactly how and where data is added or removed.

# Stacks use Last-In-First-Out; Queues use First-In-First-Out

# tacks (LIFO)
# A stack operates on a Last-In, First-Out (LIFO) principle.
# Think of a stack of plates at a buffet: you can only add a new plate
# to the top, and when someone needs a plate, they take the one off the top.
# The last plate you put down is the first one picked up.

# A python list can work as a stack

# Initialization
stack = []

# Push (Add to top)
stack.append("A")
stack.append("B")
stack.append("C")

# Peek (Look at the top element without removing it)
print(stack[-1]) # Output: "C"

# Pop (Remove and return top element)
top = stack.pop()
print(top)       # Output: "C"
print(stack)     # Output: ['A', 'B']



# Queues (FIFO)
# A queue operates on a First-In, First-Out (FIFO) principle.
# Think of a line at a grocery store checkout: the first person
# who gets in line is the first person to be served.
# New people join at the back, and people leave from the front.

# collections.deque is used for a queue, don't use a starndard python list for it.
from collections import deque

# Initialization
queue = deque()

# Enqueue (Add to the back)
queue.append("Alice")
queue.append("Bob")
queue.append("Charlie")

# Peek (Look at the front element)
print(queue[0]) # Output: "Alice"

# Dequeue (Remove and return the front element)
front = queue.popleft()
print(front)    # Output: "Alice"
print(queue)    # Output: deque(['Bob', 'Charlie'])