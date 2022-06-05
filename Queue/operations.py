class Queue:
    def __init__(self):
        self.items=[]
    
    def __str__(self):
        values=[str(x) for x in self.items]
        return ' '.join(values)
    
    def isempty(self):
        if self.items==[]:
            return True
        else:
            return False

    def enqueue(self,data):
        self.items.append(data)
    
    def dequeue(self):
        if self.isempty()==True:
            return "empty"
        else:
            return self.items.pop(0)
    
    def peek(self):
        if self.isempty()==True:
            return "empty"
        else:
            return self.items[0]

    def delete(self):
        self.items=None