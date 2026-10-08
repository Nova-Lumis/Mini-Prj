class LinkedList:
    class Node:
        def __init__(self, element):
            self.element = element
            self.next = None
        
        def __str__(self):
            return f"{self.element}"
            
    def __init__(self):
        self.length = 0
        self.head = None

    # checking whether linked list contains node
    def is_empty(self) -> bool:
        return self.length == 0

    # Add node to the linked list at last position
    def add(self, element) -> None:
        node = self.Node(element)
        if self.is_empty():
            # when empty, the first element will become the head of linked list
            self.head = node
        else:
            # Adding the node to the linked list (as last node)
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.length += 1

    # remove certain node with element provided from the current linked list
    def remove(self, element) -> None:
        # consider remove element 9
        previous_node = None
        # considered as none for previous_node
        current_node = self.head
        # rn, it is current_n -> 1

        # The loop will break, either by finding same element, or become None when the provided element is not exist. 
        while current_node is not None and current_node.element != element:
        # rn, current_node = 1, so not None, and 1 is not eq to 9
            previous_node = current_node
            # so, prev_n will be none -> 1
            current_node = current_node.next
            # the next from 1 is 9
            # Since, now the current_node element is 9 and eq to element 9, loop break

        # The current node is 9, The previous node is 1
        if current_node is None:
            return        
        elif previous_node is not None:
            # This condition is met since pn is 1 and not None
            previous_node.next = current_node.next
            # pn.next is number 9, and it is replaced with cn.next (number 8)
            # element 9 removed (the right way to say, seems the line is cutted/separated)
        else:
            self.head = current_node.next
        self.length -= 1

    # Added methods to view the current linked list
    def view(self) -> str:
        result = ""
        current_node = self.head
        while current_node is not None:
            result += f"{current_node.element}-> "
            current_node = current_node.next
        result += "None"
        return result

# Main
my_list = LinkedList()
print(my_list.is_empty())

# Adding new node element to linked list
my_list.add(1)
my_list.add(9)
my_list.add(8)
print(my_list.view())

# Remove existing node element from linked list
my_list.remove(9)
my_list.add(12)
my_list.remove(10) # Not exist
print(my_list.view())

