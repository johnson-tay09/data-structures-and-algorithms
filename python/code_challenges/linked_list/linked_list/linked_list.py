

"""
 A Node class that has properties for the value stored in the Node, and a pointer to the next Node.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self, arr=[]):
        self.head = None
        # rearrange the list for counting nth from end
        for value in arr[::-1]:
            self.insert(value)

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        # start at the head
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            # traverse list
            current_node = current_node.next
        return False

    def __str__(self):
        current_node = self.head
        string_of_values = ""
        while current_node:
            string_of_values += f" { {str(current_node.value)} } ->"
            current_node = current_node.next
        return string_of_values.replace("'", " ") + " NULL"

    def value_list(self):
        results = []
        current_node = self.head
        while (current_node):
            if (current_node.value):
                results.append(current_node.value)
            current_node = current_node.next
        return results

# add a node to the end
    def append_list(self, value):
        # create a new node with the given value
        new_node = Node(value)
        # if the list exists or has a head value of true set current node = to head
        # aka start at the head
        if(self.head):
            current_node = self.head
        # while current_node has a next value set current_node.next equal to this node
        # this should move us to the end of the list.
            while(current_node.next):
                current_node = current_node.next
            current_node.next = new_node
            # otherwise set new node equal to self.head as in the first node in the list
        else:
            self.head = new_node

        # insert a value before a given node

    def insert_before(self, target, value):
        # create a new node with the given value
        new_node = Node(value)
        # if the list exists or has a head value of true set current node = to head
        # aka start at the head
        if(self.head):
            current_node = self.head
            # if we want to add a node before the first
            if target == self.head.value:
                # set the next value of our new node to the current first node
                new_node.next = current_node
                # set the new node as head
                self.head = new_node
                # exit the fnc
                return
            # while current_node next node value is not equal to target, traverse the list
            while(current_node.next.value != target):
                # when we get to the node before our target place our new node there
                current_node = current_node.next
            # have our new node point to the target node
            new_node.next = current_node.next
            # node we are at points to new node
            current_node.next = new_node
            # otherwise set new node equal to self.head as in the first node in the list
        else:
            self.head = new_node

    # insert a value after a given node
    def insert_after(self, target, value):
        # create a new node with the given value
        new_node = Node(value)
        # if the list exists or has a head value of true set current node = to head
        # aka start at the head
        if(self.head):
            current_node = self.head
        # while current_node next node value is not equal to target, traverse the list
            while(current_node.next.value != target):
                # when we get to the node before our target place our new node there
                current_node = current_node.next
            # move forward one more node so current node = target node
            current_node = current_node.next
            # have our new node point to the target node
            new_node.next = current_node.next
            # node we are at points to new node
            current_node.next = new_node
            # otherwise set new node equal to self.head as in the first node in the list
        else:
            self.head = new_node
# track the length of the list

    def list_length(self):
        length = 0
        current_node = self.head
        # traverse the list and increment length
        while current_node:
            length += 1
            current_node = current_node.next
        return length

    def nth_from_end(self, n=0):
        # make sure user inputs an int
        if type(n) != int:
            return 'Exception'
        # make sure user inputs a number not greater than the list or negative
        if n > self.list_length() or n < 0:
            return 'Exception'
        # start at the head
        current_node = trailing = self.head
        counter = 0
        # traverse the list and increase counter
        while current_node.next:
            current_node = current_node.next
            counter += 1
            # when counter passes n the next node is the target
            if counter > n:
                trailing = trailing.next
        return trailing.value
