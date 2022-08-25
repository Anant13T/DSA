class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    
class DLL:
    def __init__(self):
        self.head=None
    
    def display(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
            while temp:
                print(temp.data)
                temp=temp.next