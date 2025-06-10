# Reverse Linked List - Detailed Explanation

## Initial Setup
Let's say we have a linked list: **A -> B -> C -> D -> NONE**

```
A -> B -> C -> D -> NONE
```

## Step-by-Step Execution

### Initial State
```python
if not self.head:
    return
```
- Checks if the list is empty. If yes, nothing to reverse.

### Initialize Variables
```python
prev = None
current = self.head
```
- `prev = None` (will point to the previous node)
- `current = A` (points to the first node)

**Visual State:**
```
prev = None
current = A -> B -> C -> D -> NONE
```

---

## Iteration 1

### Store Next Node
```python
next_temp = current.nextNode  # Store next node
```
- `next_temp = B` (saves the next node before we lose the connection)

**Visual State:**
```
prev = None
current = A -> B -> C -> D -> NONE
next_temp = B
```

### Reverse the Link
```python
current.nextNode = prev  # Reverse the link
```
- `A.nextNode = None` (A now points to None instead of B)

**Visual State:**
```
prev = None
current = A -> None
next_temp = B -> C -> D -> NONE
```

### Move Pointers Forward
```python
prev = current        # Move prev forward
current = next_temp   # Move current forward
```
- `prev = A`
- `current = B`

**Visual State:**
```
prev = A -> None
current = B -> C -> D -> NONE
```

---

## Iteration 2

### Store Next Node
```python
next_temp = current.nextNode  # Store next node
```
- `next_temp = C`

**Visual State:**
```
prev = A -> None
current = B -> C -> D -> NONE
next_temp = C
```

### Reverse the Link
```python
current.nextNode = prev  # Reverse the link
```
- `B.nextNode = A` (B now points to A)

**Visual State:**
```
prev = A -> None
current = B -> A -> None
next_temp = C -> D -> NONE
```

### Move Pointers Forward
```python
prev = current        # Move prev forward
current = next_temp   # Move current forward
```
- `prev = B`
- `current = C`

**Visual State:**
```
prev = B -> A -> None
current = C -> D -> NONE
```

---

## Iteration 3

### Store Next Node
```python
next_temp = current.nextNode  # Store next node
```
- `next_temp = D`

### Reverse the Link
```python
current.nextNode = prev  # Reverse the link
```
- `C.nextNode = B` (C now points to B)

**Visual State:**
```
prev = B -> A -> None
current = C -> B -> A -> None
next_temp = D -> NONE
```

### Move Pointers Forward
```python
prev = current        # Move prev forward
current = next_temp   # Move current forward
```
- `prev = C`
- `current = D`

**Visual State:**
```
prev = C -> B -> A -> None
current = D -> NONE
```

---

## Iteration 4 (Final)

### Store Next Node
```python
next_temp = current.nextNode  # Store next node
```
- `next_temp = None`

### Reverse the Link
```python
current.nextNode = prev  # Reverse the link
```
- `D.nextNode = C` (D now points to C)

**Visual State:**
```
prev = C -> B -> A -> None
current = D -> C -> B -> A -> None
next_temp = None
```

### Move Pointers Forward
```python
prev = current        # Move prev forward
current = next_temp   # Move current forward
```
- `prev = D`
- `current = None`

**Visual State:**
```
prev = D -> C -> B -> A -> None
current = None
```

---

## Loop Ends & Update Head

Since `current = None`, the while loop ends.

```python
self.head = prev  # Update head to the new first node
```
- `self.head = D`

## Final Result
**Original:** A -> B -> C -> D -> NONE
**Reversed:** D -> C -> B -> A -> NONE

## Key Points

1. **Three Pointers**: We use `prev`, `current`, and `next_temp` to keep track of positions
2. **Save Before Breaking**: Always store `next_temp` before breaking the link
3. **Reverse One Link**: Change `current.nextNode` to point backward
4. **Move Forward**: Advance both `prev` and `current` for next iteration
5. **Update Head**: Finally, make the last processed node the new head

## Space Complexity: O(1)
- Only uses 3 pointer variables regardless of list size
- No additional data structures needed