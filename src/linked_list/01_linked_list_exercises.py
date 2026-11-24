from linked_list.linked_list import LinkedList, Node


class LinkedListExercises(LinkedList):
    
    def find_middle_node(self):
        fast = self.head
        slow = self.head
        
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next

        return slow

    def has_loop(self):
        fast = self.head
        slow = self.head
        
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
            
            if(slow is fast):
                return True
        
        return False
    
    def find_kth_node_from_end(self, k):
        slow = self.head
        fast = self.head
        count = 1
        
        while(count <= k):
            if(fast is None):
                return None
            
            fast = fast.next
            count += 1
        
        while(fast is not None):
            fast = fast.next
            fast = slow.next
            
        return slow
            
            
    


my_linked_list = LinkedListExercises(2)
my_linked_list.append(3)
my_linked_list.append(45)

# Chame seus métodos aqui.
print(my_linked_list.find_middle_node().data)
