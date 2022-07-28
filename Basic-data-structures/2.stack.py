class Node(object):
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head = None) -> None:
        self.head = head
    
    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        if self.head:
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            return deleted_element
        else:
            return None

class Stack(object):
    def __init__(self, top=None) -> None:
        self.ll = LinkedList(top)
    
    def push(self, new_element):
        self.ll.insert_first(new_element)
    
    def pop(self):
        return self.ll.delete_first()

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

stack = Stack(e1)

stack.push(e2)
stack.push(e3)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(e4)
print(stack.pop().value)