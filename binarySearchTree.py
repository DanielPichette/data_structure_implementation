from treeNode import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # member methods
    def insert_node(self, data):
        node = TreeNode(data)
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

