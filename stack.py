class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
        self._history = Stack() 

    def push(self, element):
        new_node = Node(element)

        if self.top is not None:
            new_node.next = self.top
            self.top.prev = new_node
        
        self.top = new_node
        self._size += 1
        
        if not self._history.is_empty():
            self._history = Stack()

    def pop(self):

        if self.is_empty():
            raise IndexError("The stack is empty")
        
        removed_node = self.top
        removed_data = removed_node.data
        
        self._history.push(removed_data)
        
        self.top = self.top.next
        self._size -= 1
        
        if self.top is not None:
            self.top.prev = None
        
        return removed_data
    
    def undo_pop(self):

        if self._history.is_empty():
            print("There are no elements to return.")
            return

        last_popped_element = self._history.pop()
        self.push(last_popped_element)

        temp_history = self._history
        self._history = temp_history


    def peek(self):
        if self.is_empty():
            raise IndexError("The stack is empty")
        return self.top.data
    
    def is_empty(self):
        return self._size == 0
    
    def __len__(self): 
        return self._size
    
    def __repr__(self):
        r = ""
        pointer = self.top
        while pointer is not None:
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r
    
    def __str__(self): 
        return self.__repr__()