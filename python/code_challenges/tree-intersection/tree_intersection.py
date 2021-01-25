

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):

        # return list of values ordered correctly
        values = []

        def traverse(root):

            if not root:
                return

            values.append(root.value)
            traverse(root.left)
            traverse(root.right)

        traverse(self.root)

        print(values)

        return values

    def in_order(self):

        values = []

        def traverse(root):

            if not root:
                return

            traverse(root.left)

            values.append(root.value)
            traverse(root.right)

        traverse(self.root)

        print(values)

        return values

    def post_order(self):

        values = []

        def traverse(root):

            if not root:
                return

            traverse(root.left)
            traverse(root.right)
            # print(root.value)
            values.append(root.value)

        traverse(self.root)

        print(values)

        return values


class BinarySearchTree(BinaryTree):

    def add(self, value):
        node = Node(value)
    # check if there is no root, if so make the new node root.
        if not self.root:
            self.root = node
            return

        def traverse(root):
            if value < root.value:
               # check if the node already has a left, if not add our new node
                if not root.left:
                    root.left = node
                else:
                    # keep traverseing
                    traverse(root.left)

            else:
                # check if the node already has a right, if not add our new node
                if not root.right:
                    root.right = node
                else:
                    # keep traverseing
                    traverse(root.right)

        traverse(self.root)

    def contains(self, value):

        def search(root):
            if value == root.value:
                return True
            if value < root.value:

                if not root.left:
                    return False
                else:
                    # keep searching onto the next node
                    search(root.left)
            else:
                if not root.right:
                    return False
                else:
                    # keep searching onto the next node
                    search(root.right)

    def tree_intersection(self, tree_two):
        # array to hold the shared values
        shared_values = []
        # traverse the tree

        def traversal(root):
            if not root:
                return
            # use contains method to see if tree two has current value
            if tree_two.contains(root.value):
                # add value in common to array
                shared_values.append(root.value)
            # check left branch
            traversal(root.left)
            # check right branch
            traversal(root.right)

        traversal(self.root)
        return shared_values
