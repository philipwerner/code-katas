"""Proper paranthetics code kata module."""


class Node(object):
    """Node class for parens."""

    def __init__(self, data, previous):
        """Create a new Node."""
        self.data = data
        self.previous = previous
        self.next_node = None


class Queue(object):
    """Queue class."""

    def __init__(self):
        """Create an instance of a queue."""
        self.head = None
        self.tail = None
        self._counter = 0

    def enqueue(self, val):
        """Add a node to the queue."""
        new_tail = Node(val, self.tail)
        if self.tail is None:
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.next_node = new_tail
            self.tail = new_tail
        self._counter += 1

    def dequeue(self):
        """Remove a node from the queue."""
        if not self.head:
            raise IndexError("There is nothing to remove.")
        removed = self.head.data
        if self.head.next_node:
            self.head.next_node.previous = None
            self.head = self.head.next_node
        else:
            self.head = None
        self._counter -= 1
        return removed

    def size(self):
        """Return the size of the queue."""
        return self._counter

    def __len__(self):
        """Return the length of the queue."""
        return self._counter


def parens(data):
        """
        Will check the string for open, closed or even parens.

        If (), will return 0
        If )(, will return -1
        if ((, will return 1
        """
        q = Queue()
        data = list(data)
        bal = 0
        for i in data:
            q.enqueue(i)
        if len(q) == 0:
            raise ValueError("The string needs at least 1 paren.")
        while bal >= 0 and len(q) > 0:
            top = q.dequeue()
            if top == "(":
                bal += 1
            if top == ")":
                bal -= 1
        if bal > 1:
            return 1
        elif bal < -1:
            return -1
        else:
            return bal
