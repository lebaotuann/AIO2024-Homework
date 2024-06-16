# Section 1, Q3


class Queue:
    """This class implements a First In First Out (FIFO) data structure in Python."""

    def __init__(self, capacity: int):
        self.__capacity = capacity  # The number of elements in the queue.
        self.__queue = []

    def is_empty(self):
        """Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, otherwise is False.
        """
        return not bool(self.__queue)

    def is_full(self):
        """Check if the queue is full.

        Returns:
            bool: True if the queue is full, otherwise is False.
        """
        return len(self.__queue) == self.__capacity

    def dequeue(self):
        """Remove an element from the front of the queue.

        Returns:
            any: The element from the front of the queue.
        """
        if self.is_empty():
            return None  # queue is empty
        return self.__queue.pop(0)

    def enqueue(self, value):
        """Add an element to the end of the queue.

        Args:
            value (any): The element.
        """
        if self.is_full():
            raise IndexError("Queue overflow.")
        self.__queue.append(value)

    def front(self):
        """Get the value of the front of the queue without removing it.

        Returns:
            any: The value of the front of the queue.
        """
        if self.is_empty():
            return None  # queue is empty
        return self.__queue[0]
