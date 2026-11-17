class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


    def append(self, value):
        new_node = Node(value)
        
        if(self.head is None):
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

        return True

    def pop(self):
        if(self.head is None):
            return None
        elif(self.length == 1):
            self.head = None
            self.tail.next = None
            self.tail = None
        else:
            temp = self.head
            pre = self.head
    
            while(temp.next):
                pre = temp
                temp = temp.next

            self.tail = pre
            self.tail.next = None
            self.length -= 1
            
            return temp




my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.append(45)
print("lista inicial")
my_linked_list.print_list()
my_linked_list.pop()
print("removeu o 1")
my_linked_list.print_list()
my_linked_list.pop()
print("removeu o 2")
my_linked_list.print_list()
print("removeu o 3")
my_linked_list.pop()
my_linked_list.print_list()
