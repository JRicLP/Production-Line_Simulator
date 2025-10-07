class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Stack:
    
    def __init__(self, is_internal_history=False):
        self.top = None
        self._size = 0
        
        if not is_internal_history:
            self._history = Stack(is_internal_history=True)
        else:
            self._history = None # 

    def push(self, element, _from_undo=False):
        new_node = Node(element)

        if self.top is not None:
            new_node.next = self.top
            self.top.prev = new_node
        
        self.top = new_node
        self._size += 1
        
        if self._history is not None and not _from_undo and not self._history.is_empty():
            self._history = Stack(is_internal_history=True)

    def pop(self):
        if self.is_empty():
            raise IndexError("The stack is empty")
        
        removed_data = self.top.data
        
        if self._history is not None:
            self._history.push(removed_data)
        
        self.top = self.top.next
        self._size -= 1
        
        if self.top is not None:
            self.top.prev = None
        
        return removed_data
    
    def undo_pop(self):
        if self._history is None or self._history.is_empty():
            print("There are no elements to return.")
            return

        last_popped_element = self._history.pop()
        
        self.push(last_popped_element, _from_undo=True)

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
            r += str(pointer.data) + "\n"
            pointer = pointer.next
        return r
    
    def __str__(self): 
        return self.__repr__()