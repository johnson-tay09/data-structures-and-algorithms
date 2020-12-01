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

    def post_order(root):

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

    def find_max_value(self):
        # set current max to tree root.
        current_max = self.root
        if not self.root:
            return None

        def traverse(root):
            # pull current from above scope
            nonlocal current_max
            # empty tree edge case
            if not root:
                return
            # if root is greater than current value make the root value the current max value.
            if root.value > current_max.value:
                current_max = root
            traverse(root.left)
            traverse(root.right)

        traverse(self.root)
        return current_max.value


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
