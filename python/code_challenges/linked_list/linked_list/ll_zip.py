from linked_list.linked_list import LinkedList
"""
A zipped list weaves two linked lists together
"""


def zip_list(list_one, list_two):
    # check if lists are linked lists
    if type(list_one) != LinkedList or type(list_two) != LinkedList:
        raise TypeError
    # start at the beginning of each list
    current_one = list_one.head
    current_two = list_two.head
    # create an empty linked list
    zipped_list = LinkedList()
    # while each node has is truthy
    while current_one and current_two:
        # append method adds new node and assigns appropriate next
        zipped_list.append_list(current_one.value)
        current_one = current_one.next_
        # add list two node to zip, give it list two next
        zipped_list.append_list(current_two.value)
        current_two = current_two.next_
    remainder = current_one if current_one else current_two
    while remainder:
        zipped_list.append_list(remainder.value)
        remainder = remainder.next_
    return zipped_list
