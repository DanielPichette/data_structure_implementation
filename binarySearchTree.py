from treeNode import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # member methods
    def insert_node(self, data):
        node = TreeNode(data)
        # start at root
        current_node = self.root
        if self.root is None:
            self.root = node
            return self.root

        while self.root is not None:
            if node.data > current_node.data:
                if current_node.right_child is None:
                    current_node.right_child = node
                    node.parent = current_node.data
                    break
                else:
                    current_node = current_node.right_child

            if node.data < current_node.data:
                if current_node.left_child is None:
                    current_node.left_child = node
                    node.parent = current_node.data
                    break
                else:
                    current_node = current_node.left_child

    def search_tree(self, data):
        node = TreeNode(data)
        current_node = self.root

        while current_node is not None:
            if node.data == current_node.data:
                print('node found')
                return current_node
            elif node.data > current_node.data:
                current_node = current_node.right_child
            elif node.data < current_node.data:
                current_node = current_node.left_child
        else:
            print('node not found')

