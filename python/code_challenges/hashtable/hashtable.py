from linked_list import LinkedList


class Hashtable:

    def __init__(self, size=1024):
        self._size = size
        self._buckets = size * [None]

    def _hash(self, key):
        # declare variable for key conversion
        hash_int = 0
        # convert each ch to an int using ORD and then sum them together
        for ch in key:
            hash_int += ord(ch)
        # multiply ord value by prime num
        primed = hash_int * 19
        # set index eq to prime div by size
        index = primed % self._size
        return index

    def set(self, key, value):
        # convert the key into an index using the has method
        key_hashed = self._hash(key)
        # check if bucket w/ hashed key exists.
        if not self._buckets[key_hashed]:
            # if not, create linked list for bucket @ the index
            self._buckets[key_hashed] = LinkedList()
        # add hashed key to the bucket
        self._buckets[key_hashed].add(
            (key, value))

    def get(self, key_request):

        # hash the incoming key request
        key_hashed = self._hash(key_request)
        # set variable to the linked list at the index
        bucket_ll = self._buckets[key_hashed]
        # set variable eq to the head of the linked list
        current_head = bucket_ll.head
        # traverse the linked list
        while current_head:
            # set var eq to the tuple saved in the linked list
            kv_pair = current_head.data
            # saved key eq the tuple @ index 0 of linked list
            saved_key = kv_pair[0]
            # saved value eq the tuple @ index 1 of linked list
            saved_value = kv_pair[1]
            if saved_key == key_request:
                return saved_value
            # continue through the linked list.
            current_head = current_head.next
