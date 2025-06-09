# C++ Iterator Implementation - Complete Explanation

## What is an Iterator?

Think of an iterator like a **bookmark** in a book. You can:
- Move to the next page (++)
- Move to the previous page (--)
- Read what's on the current page (*)
- Check if two bookmarks are on the same page (==)

```cpp
// Example: Using iterators like bookmarks
std::list<int> myNumbers = {10, 20, 30, 40};
std::list<int>::iterator bookmark = myNumbers.begin();

cout << *bookmark;  // Reads "10" (first page)
bookmark++;         // Move to next page
cout << *bookmark;  // Reads "20" (second page)
```

## Why Do We Need Iterators?

**Problem**: Different containers store data differently:
- **Array**: Data stored consecutively in memory
- **Linked List**: Data scattered, connected by pointers
- **Tree**: Data in hierarchical structure

**Solution**: Iterators provide a **uniform way** to access any container:

```cpp
// SAME CODE works for different containers!
for(auto it = container.begin(); it != container.end(); it++) {
    cout << *it << endl;  // This works for list, vector, set, etc.
}
```

## const_iterator vs iterator

### const_iterator = Read-Only Bookmark
```cpp
const_iterator it;
*it = 100;  // ❌ ERROR! Can't modify data
cout << *it; // ✅ OK! Can read data
```

### iterator = Read-Write Bookmark
```cpp
iterator it;
*it = 100;  // ✅ OK! Can modify data
cout << *it; // ✅ OK! Can read data
```

### When to Use Which?
```cpp
void printList(const DList<int>& myList) {
    // Function receives const list, so must use const_iterator
    for(auto it = myList.cbegin(); it != myList.cend(); it++) {
        cout << *it;  // Can only read, not modify
    }
}

void modifyList(DList<int>& myList) {
    // Function receives non-const list, can use iterator
    for(auto it = myList.begin(); it != myList.end(); it++) {
        *it = *it * 2;  // Can modify each element
    }
}
```

## Class Hierarchy

```cpp
class const_iterator {  // Base class - read-only operations
    // Can read data but not modify
};

class iterator : public const_iterator {  // Derived class - adds write ability
    // Inherits read operations + adds write operations
};
```

**Why this hierarchy?**
```cpp
iterator it1;
const_iterator it2 = it1;  // ✅ OK! iterator can become const_iterator
// const_iterator it3;
// iterator it4 = it3;     // ❌ ERROR! const_iterator cannot become iterator
```

## Required Operations

### 1. Increment Operators (++)

**Prefix ++it** (increment first, return new value):
```cpp
DList<int> list = {10, 20, 30};
auto it = list.begin();  // Points to 10
auto result = ++it;      // it moves to 20, result also points to 20
cout << *it;             // Prints 20
cout << *result;         // Prints 20
```

**Postfix it++** (return old value, then increment):
```cpp
DList<int> list = {10, 20, 30};
auto it = list.begin();  // Points to 10
auto result = it++;      // result points to 10, it moves to 20
cout << *it;             // Prints 20
cout << *result;         // Prints 10
```

### 2. Decrement Operators (--)

Similar to increment but moves backward:
```cpp
auto it = list.end();    // Points past last element
--it;                    // Now points to last element (30)
```

### 3. Dereference Operator (*)

```cpp
auto it = list.begin();
cout << *it;             // Prints the data at current position
*it = 100;               // Modifies the data (only for iterator, not const_iterator)
```

### 4. Comparison Operators (== and !=)

```cpp
auto it1 = list.begin();
auto it2 = list.begin();
auto it3 = list.end();

cout << (it1 == it2);    // true (both point to first element)
cout << (it1 == it3);    // false (different positions)
cout << (it1 != it3);    // true (different positions)
```

## Why Store Both Node* AND DList*?

### The Problem:
```cpp
DList<int> list = {10, 20, 30};
auto it = list.end();    // Points to nullptr (past last element)
--it;                    // How do we get back to the last element (30)?
```

### The Solution:
```cpp
class const_iterator {
private:
    Node* curr_;           // Points to current node
    const DList* myList_;  // Points to the list itself
};
```

**With only Node*:**
```cpp
// At end(): curr_ = nullptr
// How to go back? No way to find the last node!
```

**With Node* AND DList*:**
```cpp
const_iterator operator--() {
    if(curr_) {
        curr_ = curr_->prev_;  // Normal case: move to previous node
    } else {
        // Special case: we're at end(), go to last node
        if(myList_) {
            curr_ = myList_->back_;  // Use list pointer to find last node
        }
    }
    return *this;
}
```

## Complete Implementation Breakdown

### const_iterator Class:

```cpp
class const_iterator {
    friend class DList;              // DList can access private members
    
private:
    const DList* myList_;            // Pointer to the list
    Node* curr_;                     // Pointer to current node
    
    // Private constructor - only DList can call this
    const_iterator(Node* curr, const DList* theList) {
        curr_ = curr;
        myList_ = theList;
    }
    
public:
    // Default constructor - creates "null" iterator
    const_iterator() {
        myList_ = nullptr;
        curr_ = nullptr;
    }
    
    // Prefix increment: ++it
    const_iterator operator++() {
        curr_ = curr_->next_;        // Move to next node
        return *this;                // Return reference to this iterator
    }
    
    // Postfix increment: it++
    const_iterator operator++(int) {  // int parameter distinguishes postfix
        const_iterator old = *this;   // Save current state
        curr_ = curr_->next_;         // Move to next node
        return old;                   // Return old state
    }
    
    // Prefix decrement: --it
    const_iterator operator--() {
        if(curr_) {
            curr_ = curr_->prev_;     // Normal case: move backward
        } else {
            // Special case: at end(), move to last element
            if(myList_) {
                curr_ = myList_->back_;
            }
        }
        return *this;
    }
    
    // Dereference: *it
    const T& operator*() const {
        return curr_->data_;          // Return reference to data
    }
    
    // Equality comparison: it1 == it2
    bool operator==(const_iterator rhs) const {
        // Two iterators are equal if they point to same node in same list
        return (myList_ == rhs.myList_ && curr_ == rhs.curr_);
    }
    
    // Inequality comparison: it1 != it2
    bool operator!=(const_iterator rhs) const {
        return !(*this == rhs);       // Just negate equality
    }
};
```

### iterator Class (Derived):

```cpp
class iterator : public const_iterator {
    friend class DList;
    
private:
    // NOTE: NO data members here!
    // We inherit curr_ and myList_ from const_iterator
    
    // Private constructor
    iterator(Node* curr, DList* theList) : const_iterator(curr, theList) {}
    
public:
    iterator() : const_iterator() {}   // Default constructor
    
    // Override increment to return iterator (not const_iterator)
    iterator operator++() {
        this->curr_ = this->curr_->next_;  // Need this-> because of inheritance
        return *this;
    }
    
    // Override dereference to allow modification
    T& operator*() {
        return this->curr_->data_;         // Return non-const reference
    }
    
    // Also provide const version
    const T& operator*() const {
        return this->curr_->data_;
    }
};
```

### DList Functions:

```cpp
// Return const_iterator to first element
const_iterator cbegin() const {
    return const_iterator(front_, this);
}

// Return const_iterator past last element
const_iterator cend() const {
    return const_iterator(nullptr, this);
}

// Return iterator to first element
iterator begin() {
    return iterator(front_, this);
}

// Return iterator past last element
iterator end() {
    return iterator(nullptr, this);
}
```

## Usage Examples:

### Example 1: Reading a List
```cpp
DList<int> myList = {10, 20, 30};

// Using const_iterator (read-only)
for(auto it = myList.cbegin(); it != myList.cend(); ++it) {
    cout << *it << " ";  // Prints: 10 20 30
}
```

### Example 2: Modifying a List
```cpp
DList<int> myList = {10, 20, 30};

// Using iterator (can modify)
for(auto it = myList.begin(); it != myList.end(); ++it) {
    *it *= 2;  // Double each value
}
// Now list contains: {20, 40, 60}
```

### Example 3: The end() Special Case
```cpp
DList<int> myList = {10, 20, 30};

auto it = myList.end();    // Points past last element (nullptr)
--it;                      // Moves to last element (30)
cout << *it;               // Prints: 30

++it;                      // Back to end()
--it;                      // Back to last element again
cout << *it;               // Prints: 30
```

This iterator implementation allows you to traverse your linked list just like any STL container!