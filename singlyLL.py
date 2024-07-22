class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
 
class SLL:
    def __init__(self) -> None:
        self.head = None
    def display(self):
        if self.head is None:
            print("empty single linked list")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end="")
                temp = temp.next
            print()
    
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head =  prev
    def add_begining(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next= self.head
            self.head = new_node
    def add_ending(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
    def add_position(self,pos,data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            cur = self.head
            for i in range(1,pos):
                cur = cur.next
            temp = cur.next
            new_node.next = temp
            cur.next = new_node

    def rotation(self):
        if self.head is None:
            print("Empty linked list")
        else:
            cur = self.head
            prev = None
            while cur:
                new_node =cur.next
                cur.next = prev 
                prev = cur
                cur = new_node
            self.head = prev
    def delete_begining(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp = self.head.next
            print("Delete at the begining",self.head.data)
            self.head = temp
    def delete_ending(self):
        prev = self.head
        temp = self.head.next
        while temp.next:
            temp = temp.next 
            prev = prev.next 
        prev.next = None
    def delete_position(self,pos):
        prev = self.head
        temp = self.head.next
        for i in range(1,pos):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        
L = SLL()
n1 = Node(10)
L.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.next = n4
L.add_ending(50)
L.display()
L.add_position(3,35)
L.display()
L.add_begining(11)
L.display()
# L.delete_begining()
# L.display()
# L.delete_ending()
L.delete_position(3)
L.display()
# L.rotation()

