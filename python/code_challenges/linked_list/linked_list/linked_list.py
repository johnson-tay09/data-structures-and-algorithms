

"""
 A Node class that has properties for the value stored in the Node, and a pointer to the next Node.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current_place = self.head
        while current_place:
            if current_place.value == value:
                return True
            current_place = current_place.next
        return False

    def __str__(self):
        current_place = self.head
        string_of_values = ""
        while current_place:
            string_of_values += f" { {str(current_place.value)} } ->"
            current_place = current_place.next
        return string_of_values.replace("'", " ") + " NULL"

    def value_list(self):
        results = []
        current_place = self.head
        while (current_place):
            if (current_place.value):
                results.append(current_place.value)
            current_place = current_place.next
        return results

    def __repr__(self):
        return self.to_string()
