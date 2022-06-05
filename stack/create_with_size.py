class Stack:
    def __init__(self,maxsize):
        self.list=[]
        self.maxsize=maxsize

    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)

    def isempty(self):
        if self.list==[]:
            return True
        else:
            return False

    def isfull(self):
        if len(self.list)==self.maxsize:
            return True
        else:
            return False

    def push(self,data):
        if self.isfull()==True:
            return "no space"
        else:
            self.list.push(data)

    def pop(self):
        if self.isempty()==True:
            return "empty stack"
        else:
            self.list.pop()
    
    def peek(self):
        if self.isempty()==True:
            return "the stack is empty"
        else:
            return self.list[len(self.list)-1]

    def delete(self):
        self.list=None