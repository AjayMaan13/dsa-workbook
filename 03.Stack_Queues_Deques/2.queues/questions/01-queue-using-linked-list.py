'''
3. Queue Using Linked List

Problem Statement: Implement a First-In-First-Out (FIFO) queue using a singly linked list.

Operations:
- push(x)   : Adds element x to the end of the queue.
- pop()     : Removes and returns the front element. Returns -1 if empty.
- peek()    : Returns the front element without removing it. Returns -1 if empty.
- isEmpty() : Returns True if the queue is empty, False otherwise.

Examples:
    Input:  ["LinkedListQueue", "push", "push", "peek", "pop", "isEmpty"]
            [[], [3], [7], [], [], []]
    Output: [None, None, None, 3, 3, False]

    Input:  ["LinkedListQueue", "push", "pop", "isEmpty"]
            [[], [2], [], []]
    Output: [None, None, 2, True]

Approach:
- front pointer = head of the list (dequeue from here)
- rear pointer  = tail of the list (enqueue here)
- push : new node linked at rear, rear moves forward      O(1)
- pop  : save front.val, move front to front.next         O(1)
- peek : return front.val                                 O(1)

Time Complexity : O(1) for all operations
Space Complexity: O(n)
'''


class Node:
    def __init__(self, d):
        self.val = d
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.front = None  # head — dequeue from here
        self.rear = None   # tail — enqueue here
        self.size = 0

    def push(self, x):
        element = Node(x)
        if self.rear is None:           # queue is empty
            self.front = self.rear = element
        else:
            self.rear.next = element    # link new node at the end
            self.rear = element         # move rear forward
        self.size += 1

    def pop(self):
        if self.front is None:
            return -1
        value = self.front.val
        self.front = self.front.next    # move front forward
        if self.front is None:          # queue became empty
            self.rear = None
        self.size -= 1
        return value

    def peek(self):
        if self.front is None:
            return -1
        return self.front.val

    def isEmpty(self):
        return self.front is None


# --- Driver ---
q = LinkedListQueue()

commands = ["LinkedListQueue", "push", "push", "peek", "pop", "isEmpty"]
inputs   = [[], [3], [7], [], [], []]

results = []
for cmd, args in zip(commands, inputs):
    if cmd == "LinkedListQueue":
        results.append(None)
    elif cmd == "push":
        q.push(args[0])
        results.append(None)
    elif cmd == "pop":
        results.append(q.pop())
    elif cmd == "peek":
        results.append(q.peek())
    elif cmd == "isEmpty":
        results.append(q.isEmpty())

print(results)  # [None, None, None, 3, 3, False]
