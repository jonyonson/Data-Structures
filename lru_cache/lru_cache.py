from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.dll = DoublyLinkedList()
        self.storage = {}
        self.current_size = 0

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key not in self.storage:
            return None

        new_node = self.storage[key]
        # make most recently used
        self.dll.move_to_end(new_node)
        return new_node.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):

        if key not in self.storage:
            self.dll.add_to_tail((key, value))
            self.storage[key] = self.dll.tail
            self.current_size += 1

        # overwrite the old value associated with the key
        node = self.storage[key]
        node.value = (key, value)
        self.dll.move_to_end(node)

        # if self.current_size == self.limit:
        #     # add the oldest entry in the cache


# cache = LRUCache(3)
# cache.set('item1', 'a')
# cache.set('item1', 'b')
# print(cache.get('item1'))
