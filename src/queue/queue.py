class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self, data):
        new_node = Node(data)
        self.first = new_node
        self.last = new_node
        self.length = 1
        
    def enqueue(self, data):
        new_node = Node(data)
        
        if(self.first is None):
            self.first = new_node
            self.last = new_node
        
        else:
            self.last.next = new_node
            self.last = new_node
            
        self.length +=1
        
    def dequeue(self):            
        if self.length == 0:
            return None

        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
            
        self.length -=1
        return temp        
        
        
    
    def print_queue(self):
        temp = self.first
        
        while(temp is not None):        
            print(temp.data)
            temp = temp.next
        

if __name__ == "__main__":             
    my_stack = Queue(6)
    my_stack.enqueue(4)
    my_stack.dequeue()
    my_stack.dequeue()
    my_stack.print_queue()
