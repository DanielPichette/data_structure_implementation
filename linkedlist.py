from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        temporary_node = self.head

        while temporary_node.next is not None:
            temporary_node = temporary_node.next

        temporary_node.next = node

    # PROBLEM 3:
    # ake the already created linked list with an append_node method and add on the following functionality:
    # a : add_to_beginning:

    def add_to_beginning(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            if self.head is not None:
                node.next = self.head
                self.head = node
                return

    # b : contains_node

    def contains_node(self, data):
        current_node = self.head
        while current_node.next is not None:
            if current_node.data == data:
                print('value found')
                return True
            else:
                current_node = current_node.next
