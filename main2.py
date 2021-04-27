from linkedlist import LinkedList

if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)
    linked_list.add_to_beginning(45)
    linked_list.add_to_beginning(43)
    linked_list.add_to_beginning(30)

    linked_list.contains_node(55)
