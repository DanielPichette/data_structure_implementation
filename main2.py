from linkedlist import LinkedList
from binarySearchTree import BinarySearchTree
if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)
# PROBLEM 3a
    linked_list.add_to_beginning(45)
    linked_list.add_to_beginning(43)
    linked_list.add_to_beginning(30)
# PROBLEM 3b
    linked_list.contains_node(5)
# PROBLEM 4
    tree = BinarySearchTree()
# PROBLEM 4a
    tree.insert_node(10)
    tree.insert_node(5)
    tree.insert_node(3)
    tree.insert_node(13)
    tree.insert_node(11)
