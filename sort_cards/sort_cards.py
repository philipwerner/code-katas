"""Sorting cards using a priority Q."""


class Node(object):
    """A Node which contains a value."""

    def __init__(self, data):
        """Create a new node with priority assigned."""
        self.data = data
        self.prev = None
        self.next = None
        if self.data is 'A':
            self.priority = 1
        elif self.data is 'T':
            self.priority = 11
        elif self.data is 'J':
            self.priority = 12
        elif self.data is 'Q':
            self.priority = 13
        elif self.data is 'K':
            self.priority = 14
        else:
            int(data)
            self.priority = int(data)


class PQ(object):
    """A Line of Nodes."""

    def __init__(self, iterable=()):
        """Create an empty queue."""
        self.head = None
        self.tail = None
        self._counter = 0
        if hasattr(iterable, '__iter__') or isinstance(iterable, str):
            for item in iterable:
                self.insert(item)

    def insert(self, val):
        """Add a node to the tail of the queue."""
        new_node = Node(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        while new_node.prev and new_node.priority < new_node.prev.priority:
            temp = new_node.prev
            if new_node.prev.prev:
                    new_node.prev.prev.next = new_node
                    new_node.prev = new_node.prev.prev
            else:
                new_node.prev = None
                self.head = new_node
            if new_node.next:
                temp.next = new_node.next
                temp.next.prev = temp
            else:
                self.tail = temp
                temp.next = None
            new_node.next = temp
            new_node.next.prev = new_node

        self._counter += 1

    def return_list(self):
        """To match the kata request."""
        if self.head is None:
            return
        the_list = []
        the_node = self.head
        while the_node:
            the_list.append(str(the_node.data))
            the_node = the_node.next
        return the_list


def sort_cards(cards):
    """Sort the cards."""
    q = PQ(cards)
    return q.return_list()
