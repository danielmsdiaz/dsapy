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

    def prepend(self, value):
        new_node = Node(value)
        if self.length < 1:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp

        self.length += 1
        return True

    def pop_first(self):
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        self.length -= 1
        return True

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        count = 0
        temp = self.head

        while count < index:
            temp = temp.next
            count += 1

        print("get: ", temp.data)
        return temp

    def insert(self, index, value):
        if(index < 0 or index > self.length):
            return False
        
        if(index == 0):
            return self.prepend(value)
        
        if(index == self.length):
            return self.append(value)
        
        new_node = Node(value)
        previous = self.get(index - 1)
        new_node.next = previous.next
        previous.next = new_node
        self.length += 1
        return True,
    
    def remove(self, index):
            if(index < 0 or index >= self.length):
                return None
            
            if(index == 0):
                return self.pop_first()
            
            if(index == self.length - 1):
                return self.pop()
            
            previous = self.get(index - 1)
            actual = previous.next
            previous.next = actual.next
            actual.next = None
            self.length -= 1
            return True
        
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        

    # def set_value(self, index, value):
    #         if index < 0 or index >= self.length:
    #             return None

    #         count = 0
    #         temp = self.head

    #         while count < index:
    #             temp = temp.next
    #             count += 1

    #         print("valor inicial: ", temp.data)
    #         temp.data = value
    #         print("valor alterado: ", temp.data)
    #         return temp

    def set_value(self, index, value):
        temp = self.get(index)

        if temp is None:
            return False
        else:
            temp.data = value

        print("valor inicial: ", temp.data)
        temp.data = value
        print("valor alterado: ", temp.data)
        return temp

    def pop(self):
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail.next = None
            self.tail = None
        else:
            temp = self.head
            pre = self.head

            while temp.next:
                pre = temp
                temp = temp.next

            self.tail = pre
            self.tail.next = None
            self.length -= 1

            return temp


my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.append(45)
my_linked_list.reverse()
my_linked_list.print_list()
# print("lista inicial")
# my_linked_list.print_list()
# my_linked_list.pop()
# print("removeu o 1")
# my_linked_list.print_list()
# my_linked_list.pop()
# print("removeu o 2")
# my_linked_list.print_list()
# print("adicionou no inicio")
# my_linked_list.prepend(10)
# my_linked_list.print_list()
# print("adicionou no inicio")
# my_linked_list.prepend(9)
# my_linked_list.print_list()
# print("removeu o ultimo")
# my_linked_list.pop()
# my_linked_list.print_list()
# print("removeu o primeiro")
# my_linked_list.pop_first()
# my_linked_list.print_list()
