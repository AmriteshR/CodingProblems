class Node():
    def __init__(self, value) -> None:
        # print(f"Creating Node of value {value}")
        self.data = value
        self.next = None
    
    def __repr__(self):
        return str(self.data)

        
class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def is_empty_list(self):
        return self.head is None
    
    def __iter__(self):
        if self.is_empty_list():
            return

        start = self.head
        while start is not None:
            yield start
            start = start.next

    def __repr__(self) -> str:
        nodes = []
        for node in self:
            nodes.append(str(node.data))
        return '->'.join(nodes)
    
    def add_to_start(self, node):
        node.next = self.head
        self.head = node

    def add_to_end(self, node):
        if self.is_empty_list():
            self.head = node
            return
     
        for curr_node in self:
            pass
        curr_node.next = node

    def add_before_node(self, node, target):
        if self.is_empty_list():
            print(f"Emtpy List !")
            return

        prev_node = self.head
        for curr_node in self:
            if curr_node.data == target:
                prev_node.next = node
                node.next = curr_node
                return
            prev_node = curr_node
        raise Exception(f"Node with value {target} not found in list.")

    def add_after_node(self, node, target):
        if self.is_empty_list():
            print(f"Empty List!")
            return

        for curr_node in self:
            if curr_node.data == target:
                node.next = curr_node.next
                curr_node.next = node
                return
        raise Exception(f"Node with value {target} not found in list.")

    def init_from_list(self, node_list):
        if not node_list:
            raise Exception(f"List provided is empty!")
        
        for i in node_list:
            node = Node(i)
            self.add_to_start(node)

    def __delitem__(self,target):
        if self.is_empty_list():
            raise Exception(f"Empty List!")

        prev_node = self.head
        for curr in self:
            if curr.data == target:
                prev_node.next = curr.next
                return
            prev_node = curr
        raise Exception(f"Node with value {target} not found in list.")

class DNode():
    def __init__(self, value) -> None:
        self.data = value
        self.prev = None
        self.next = None
    
    def __repr__(self):
        return str(self.data)
    

class DoublyLinkedList():
    def __init__(self) -> None:
        self.head = None

    def is_empty_list(self):
        return self.head is None
    
    def __iter__(self):
        if self.is_empty_list():
            return

        start = self.head
        while start is not None:
            yield start
            start = start.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(str(node.data))
        return '->'.join(nodes)

    def add_to_start(self, node):
        if self.is_empty_list():
            self.head = node
            return
        
        
# ll = LinkedList()
# # values = [1,2,3,4,5]
# # ll.init_from_list(values)
# print(ll)
# ll.add_to_end(Node(9))
# print(ll)
# ll.add_before_node(Node(11),2)
# print(ll)
# ll.add_after_node(Node(12),4)
# print(ll)
# del ll[2]
# print(ll)