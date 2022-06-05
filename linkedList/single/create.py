class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Slinked:
    def __init__(self):
        self.head=None
    
    def display(self):
        temp=self.head
        if self.head is None:
            print("Empty")
        else:
            while temp:
                print(temp.data)
                temp=temp.next

s1=Slinked()
n1=Node(10)
n2=Node(20)
n3=Node(30)
s1.head=n1
n1.next=n2
n2.next=n3
s1.display()