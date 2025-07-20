class LinkedList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.nextNode = None
        def __str__(self):
            return self.data

    def __init__(self, data):
        self.head = None

    def add(self, data):
        """Add element to the end of the list. O(n)"""
        new_node = self.Node(data)
        
        if (self.head == None):
            self.head = new_node
        else:
            current = self.head
            while current.nextNode:
                current = current.nextNode
            current.nextNode = new_node
        
    
    def __str__(self):
        pointer = self.head
        while pointer.nextNode:
            print(f'{pointer} -> ', end=' ')
            pointer = pointer.nextNode
            
        print(f'{pointer} -> NONE', end=' ')
        print()
            

def reverseLL(self):

        # Edge Case
        if self.head == None or self.head.nextNode == None:
            return self

        endPointer = self.head
        while endPointer.nextNode:
            endPointer = endPointer.nextNode
        
        print(f"endPoint of LL found, data: {endPointer}")
        
    

        startPointer = self.head

        print(f'StartPointer: {startPointer}, endPointer: {endPointer}')
        self.head = self.head.nextNode 
        endPointer.nextNode = startPointer
        endPointer.nextNode.nextNode = None
        startPointer = self.head

        print(self)
        
        while endPointer != startPointer:
             self.head = self.head.nextNode
             startPointer.nextNode = endPointer.nextNode
             endPointer.nextNode = startPointer

             startPointer = self.head
             print(self)


        
        print(f'StartPointer: {startPointer}, endPointer: {endPointer}')

        print(self)
        return self          

if __name__ == "__main__":
    ll = LinkedList(None)

    # Add 5 elements using the add method
    ll.add("A")
    ll.add("B")
    ll.add("C")
    ll.add("D")
    ll.add("E")

    # Print the linked list
    #ll.__str__()
    #print(ll)

    reverseLL(ll)
