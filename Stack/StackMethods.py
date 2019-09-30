class Stack():
    def __init__(self):
        self.stack=[]

    def push(self):
        self.stack.append(30)
        self.stack.append(40)
        self.stack.append(50)
        print(self.stack)
    def pop(self):
        print(self.stack.pop())
        self.stack.sort()
        print(self.stack)

l=Stack()
l.push()
l.pop()