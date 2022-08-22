class Node :
    def __init__(self, data = 0, next= None):
        self.data = data
        self.next = next

class Stack :
    def __init__(self):
        self.head = None
    
    def push(self, data) :
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if slef.is_empty():
            return -1
        data = self.head.data
        self.head = self.head.next
        return data
    
    def is_empty(self):
        if self.head :
            return False
        return True

    def peek(self):
        if self.is_empty():
            return -1
        return self.head.data