#include <stdio.h>
#include <stdlib.h>

// =============================================================================
// SINGLY LINKED LIST IMPLEMENTATION
// =============================================================================

// Node structure for singly linked list
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Singly Linked List structure
typedef struct LinkedList {
    Node* head;
    int size;
} LinkedList;

// Function prototypes for Singly Linked List
LinkedList* createList();
void insertFront(LinkedList* list, int data);
void insertBack(LinkedList* list, int data);
void insertAt(LinkedList* list, int index, int data);
void deleteFront(LinkedList* list);
void deleteBack(LinkedList* list);
void deleteAt(LinkedList* list, int index);
int search(LinkedList* list, int data);
void printList(LinkedList* list);
void freeList(LinkedList* list);

// =============================================================================
// SINGLY LINKED LIST IMPLEMENTATIONS
// =============================================================================

// Create a new empty linked list
LinkedList* createList() {
    LinkedList* list = (LinkedList*)malloc(sizeof(LinkedList));
    if (list == NULL) {
        printf("Memory allocation failed!\n");
        return NULL;
    }
    list->head = NULL;
    list->size = 0;
    return list;
}

// Insert at the front of the list
void insertFront(LinkedList* list, int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Memory allocation failed!\n");
        return;
    }
    
    newNode->data = data;
    newNode->next = list->head;
    list->head = newNode;
    list->size++;
}

// Insert at the back of the list
void insertBack(LinkedList* list, int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Memory allocation failed!\n");
        return;
    }
    
    newNode->data = data;
    newNode->next = NULL;
    
    if (list->head == NULL) {
        list->head = newNode;
    } else {
        Node* current = list->head;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
    }
    list->size++;
}

// Insert at a specific index
void insertAt(LinkedList* list, int index, int data) {
    if (index < 0 || index > list->size) {
        printf("Invalid index!\n");
        return;
    }
    
    if (index == 0) {
        insertFront(list, data);
        return;
    }
    
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Memory allocation failed!\n");
        return;
    }
    
    newNode->data = data;
    
    Node* current = list->head;
    for (int i = 0; i < index - 1; i++) {
        current = current->next;
    }
    
    newNode->next = current->next;
    current->next = newNode;
    list->size++;
}

// Delete from front
void deleteFront(LinkedList* list) {
    if (list->head == NULL) {
        printf("List is empty!\n");
        return;
    }
    
    Node* temp = list->head;
    list->head = list->head->next;
    free(temp);
    list->size--;
}

// Delete from back
void deleteBack(LinkedList* list) {
    if (list->head == NULL) {
        printf("List is empty!\n");
        return;
    }
    
    if (list->head->next == NULL) {
        free(list->head);
        list->head = NULL;
        list->size--;
        return;
    }
    
    Node* current = list->head;
    while (current->next->next != NULL) {
        current = current->next;
    }
    
    free(current->next);
    current->next = NULL;
    list->size--;
}

// Search for a value
int search(LinkedList* list, int data) {
    Node* current = list->head;
    int index = 0;
    
    while (current != NULL) {
        if (current->data == data) {
            return index;
        }
        current = current->next;
        index++;
    }
    
    return -1; // Not found
}

// Print the list
void printList(LinkedList* list) {
    printf("List: ");
    Node* current = list->head;
    while (current != NULL) {
        printf("%d", current->data);
        if (current->next != NULL) {
            printf(" -> ");
        }
        current = current->next;
    }
    printf(" -> NULL\n");
    printf("Size: %d\n\n", list->size);
}

// Free the entire list
void freeList(LinkedList* list) {
    Node* current = list->head;
    while (current != NULL) {
        Node* temp = current;
        current = current->next;
        free(temp);
    }
    free(list);
}

// =============================================================================
// DOUBLY LINKED LIST IMPLEMENTATION
// =============================================================================

// Node structure for doubly linked list
typedef struct DNode {
    int data;
    struct DNode* next;
    struct DNode* prev;
} DNode;

// Doubly Linked List structure
typedef struct DoublyLinkedList {
    DNode* head;
    DNode* tail;
    int size;
} DoublyLinkedList;

// Function prototypes for Doubly Linked List
DoublyLinkedList* createDList();
void insertDFront(DoublyLinkedList* list, int data);
void insertDBack(DoublyLinkedList* list, int data);
void insertDAt(DoublyLinkedList* list, int index, int data);
void deleteDFront(DoublyLinkedList* list);
void deleteDBack(DoublyLinkedList* list);
void deleteDAt(DoublyLinkedList* list, int index);
int searchD(DoublyLinkedList* list, int data);
void printDList(DoublyLinkedList* list);
void printDListReverse(DoublyLinkedList* list);
void freeDList(DoublyLinkedList* list);

// =============================================================================
// DOUBLY LINKED LIST IMPLEMENTATIONS
// =============================================================================

// Create a new empty doubly linked list
DoublyLinkedList* createDList() {
    DoublyLinkedList* list = (DoublyLinkedList*)malloc(sizeof(DoublyLinkedList));
    if (list == NULL) {
        printf("Memory allocation failed!\n");
        return NULL;
    }
    list->head = NULL;
    list->tail = NULL;
    list->size = 0;
    return list;
}

// Insert at the front of the doubly linked list
void insertDFront(DoublyLinkedList* list, int data) {
    DNode* newNode = (DNode*)malloc(sizeof(DNode));
    if (newNode == NULL) {
        printf("Memory allocation failed!\n");
        return;
    }
    
    newNode->data = data;
    newNode->prev = NULL;
    newNode->next = list->head;
    
    if (list->head == NULL) {
        // Empty list
        list->head = newNode;
        list->tail = newNode;
    } else {
        list->head->prev = newNode;
        list->head = newNode;
    }
    list->size++;
}

// Insert at the back of the doubly linked list
void insertDBack(DoublyLinkedList* list, int data) {
    DNode* newNode = (DNode*)malloc(sizeof(DNode));
    if (newNode == NULL) {
        printf("Memory allocation failed!\n");
        return;
    }
    
    newNode->data = data;
    newNode->next = NULL;
    newNode->prev = list->tail;
    
    if (list->tail == NULL) {
        // Empty list
        list->head = newNode;
        list->tail = newNode;
    } else {
        list->tail->next = newNode;
        list->tail = newNode;
    }
    list->size++;
}

// Insert at a specific index in doubly linked list
void insertDAt(DoublyLinkedList* list, int index, int data) {
    if (index < 0 || index > list->size) {
        printf("Invalid index!\n");
        return;
    }
    
    if (index == 0) {
        insertDFront(list, data);
        return;
    }
    
    if (index == list->size) {
        insertDBack(list, data);
        return;
    }
    
    DNode* newNode = (DNode*)malloc(sizeof(DNode));
    if (newNode == NULL) {
        printf("Memory allocation failed!\n");
        return;
    }
    
    newNode->data = data;
    
    DNode* current = list->head;
    for (int i = 0; i < index; i++) {
        current = current->next;
    }
    
    newNode->next = current;
    newNode->prev = current->prev;
    current->prev->next = newNode;
    current->prev = newNode;
    list->size++;
}

// Delete from front of doubly linked list
void deleteDFront(DoublyLinkedList* list) {
    if (list->head == NULL) {
        printf("List is empty!\n");
        return;
    }
    
    DNode* temp = list->head;
    
    if (list->head == list->tail) {
        // Only one element
        list->head = NULL;
        list->tail = NULL;
    } else {
        list->head = list->head->next;
        list->head->prev = NULL;
    }
    
    free(temp);
    list->size--;
}

// Delete from back of doubly linked list
void deleteDBack(DoublyLinkedList* list) {
    if (list->tail == NULL) {
        printf("List is empty!\n");
        return;
    }
    
    DNode* temp = list->tail;
    
    if (list->head == list->tail) {
        // Only one element
        list->head = NULL;
        list->tail = NULL;
    } else {
        list->tail = list->tail->prev;
        list->tail->next = NULL;
    }
    
    free(temp);
    list->size--;
}

// Search in doubly linked list
int searchD(DoublyLinkedList* list, int data) {
    DNode* current = list->head;
    int index = 0;
    
    while (current != NULL) {
        if (current->data == data) {
            return index;
        }
        current = current->next;
        index++;
    }
    
    return -1; // Not found
}

// Print doubly linked list forward
void printDList(DoublyLinkedList* list) {
    printf("DList (forward): NULL <- ");
    DNode* current = list->head;
    while (current != NULL) {
        printf("%d", current->data);
        if (current->next != NULL) {
            printf(" <-> ");
        }
        current = current->next;
    }
    printf(" -> NULL\n");
    printf("Size: %d\n\n", list->size);
}

// Print doubly linked list in reverse
void printDListReverse(DoublyLinkedList* list) {
    printf("DList (reverse): NULL <- ");
    DNode* current = list->tail;
    while (current != NULL) {
        printf("%d", current->data);
        if (current->prev != NULL) {
            printf(" <-> ");
        }
        current = current->prev;
    }
    printf(" -> NULL\n\n");
}

// Free the entire doubly linked list
void freeDList(DoublyLinkedList* list) {
    DNode* current = list->head;
    while (current != NULL) {
        DNode* temp = current;
        current = current->next;
        free(temp);
    }
    free(list);
}

// =============================================================================
// MAIN FUNCTION - DEMONSTRATION
// =============================================================================

int main() {
    printf("=== SINGLY LINKED LIST DEMO ===\n");
    
    // Create singly linked list
    LinkedList* list = createList();
    
    // Test insertions
    printf("Inserting 10, 20, 30 at front:\n");
    insertFront(list, 10);
    insertFront(list, 20);
    insertFront(list, 30);
    printList(list);
    
    printf("Inserting 40, 50 at back:\n");
    insertBack(list, 40);
    insertBack(list, 50);
    printList(list);
    
    printf("Inserting 25 at index 2:\n");
    insertAt(list, 2, 25);
    printList(list);
    
    // Test search
    printf("Searching for 25: Index %d\n", search(list, 25));
    printf("Searching for 100: Index %d\n\n", search(list, 100));
    
    // Test deletions
    printf("Deleting from front:\n");
    deleteFront(list);
    printList(list);
    
    printf("Deleting from back:\n");
    deleteBack(list);
    printList(list);
    
    freeList(list);
    
    printf("\n=== DOUBLY LINKED LIST DEMO ===\n");
    
    // Create doubly linked list
    DoublyLinkedList* dlist = createDList();
    
    // Test insertions
    printf("Inserting 100, 200, 300 at front:\n");
    insertDFront(dlist, 100);
    insertDFront(dlist, 200);
    insertDFront(dlist, 300);
    printDList(dlist);
    
    printf("Inserting 400, 500 at back:\n");
    insertDBack(dlist, 400);
    insertDBack(dlist, 500);
    printDList(dlist);
    
    printf("Inserting 250 at index 2:\n");
    insertDAt(dlist, 2, 250);
    printDList(dlist);
    
    // Print reverse
    printf("Printing in reverse:\n");
    printDListReverse(dlist);
    
    // Test deletions
    printf("Deleting from front:\n");
    deleteDFront(dlist);
    printDList(dlist);
    
    printf("Deleting from back:\n");
    deleteDBack(dlist);
    printDList(dlist);
    
    freeDList(dlist);
    
    return 0;
}