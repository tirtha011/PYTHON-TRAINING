'''
Implement the stack data structure using Object Oriented Programming in python. A sample class
prototype is given below:
3
class stack(object):
 def __init__(self, depth):
 self.depth = depth
 def push(self, item):
 pass
 def pop(self):
 pass
Test the class with several test cases to check the integrity of the implementation. 

'''

class Stack(object):
    def __init__(self, depth):
        self.depth = depth
        self.items = []

    def push(self, item):
        if len(self.items) < self.depth:
            self.items.append(item)
        else:
            raise OverflowError("Stack is full")

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            raise UnderflowError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0


# Test the class with several test cases
stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 

print(stack.is_empty()) 