class Stack:
    def __init__(self):
        self.list=[]

    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)

    #to check weather stack is empty or not
    def isempty(self):
        if self.list==[]:
            return True
        else:
            return False
    
    #push
    def push(self,data):
        self.list.append(data)

    #pop
    def pop(self):
        if self.isempty()==True:
            return "the stack is already empty"
        else:
            return self.list.pop()
    
    #peek
    def peek(self):
        if self.isempty()==True:
            return "the stack is empty"
        else:
            return self.list[len(self.list)-1]
    
    #delete
    def delete(self):
        self.list=None

s1=Stack()
s1.push(12)
s1.push(14)
s1.push(87)
s1.pop()
#print(s1.isempty())
#print(s1.peek())
print(s1)