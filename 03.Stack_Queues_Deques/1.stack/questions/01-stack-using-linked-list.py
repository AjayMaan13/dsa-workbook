'''
4. Stack Using Linked List

Problem Statement: Implement a Last-In-First-Out (LIFO) stack using a singly linked list.

Operations:
- push(x)   : Pushes element x onto the stack.
- pop()     : Removes and returns the top element. Returns -1 if empty.
- top()     : Returns the top element without removing it. Returns -1 if empty.
- isEmpty() : Returns True if the stack is empty, False otherwise.

Examples:
    Input:  ["LinkedListStack", "push", "push", "pop", "top", "isEmpty"]
            [[], [3], [7], [], [], []]
    Output: [None, None, None, 7, 3, False]

    Input:  ["LinkedListStack", "isEmpty"]
            [[]]
    Output: [None, True]

Approach:
- head of the linked list = top of the stack
- push : new node -> next = head, head = new node       O(1)
- pop  : save head.val, move head to head.next          O(1)
- top  : return head.val                                O(1)

Time Complexity : O(1) for all operations
Space Complexity: O(n)
'''


class Node:
    def __init__(self, d):
        self.val = d
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.head = None  # top of stack
        self.size = 0

    def push(self, x):
        element = Node(x)
        element.next = self.head  # new node points to current top
        self.head = element       # new node becomes the top
        self.size += 1

    def pop(self):
        if self.head is None:
            return -1
        value = self.head.val
        self.head = self.head.next
        self.size -= 1
        return value

    def top(self):
        if self.head is None:
            return -1
        return self.head.val

    def isEmpty(self):
        return self.size == 0


# --- Driver ---
st = LinkedListStack()

commands = ["LinkedListStack", "push", "push", "pop", "top", "isEmpty"]
inputs   = [[], [3], [7], [], [], []]

results = []
for cmd, args in zip(commands, inputs):
    if cmd == "LinkedListStack":
        results.append(None)
    elif cmd == "push":
        st.push(args[0])
        results.append(None)
    elif cmd == "pop":
        results.append(st.pop())
    elif cmd == "top":
        results.append(st.top())
    elif cmd == "isEmpty":
        results.append(st.isEmpty())

print(results)  # [None, None, None, 7, 3, False]
