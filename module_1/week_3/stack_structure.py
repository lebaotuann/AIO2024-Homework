# Section 1, Q3


class Stack:
    """This class implements a Last-In-First-Out (LIFO) data structure in Python."""

    def __init__(self, capacity: int):
        self.__capacity = capacity  # The number of elements in the stack.
        self.__stack = []

    def is_empty(self):
        """Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, otherwise is False.
        """
        return not bool(self.__stack)

    def is_full(self):
        """Check if the stack is full.

        Returns:
            bool: True if the stack is full, otherwise is False.
        """
        return len(self.__stack) == self.__capacity

    def pop(self):
        """Remove an element from the top of a stack.

        Returns:
            any: The element from the top of a stack.
        """
        if self.is_empty():
            return None  # stack is empty
        return self.__stack.pop()

    def push(self, value):
        """Add an element to the top of a stack.

        Args:
            value (any): The new value to add to the stack.
        """
        if self.is_full():
            raise IndexError("Stack overflow.")
        self.__stack.append(value)

    def top(self):
        """Get the value of the top element without removing it.

        Returns:
            any: The value of the top element.
        """
        if self.is_empty():
            return None  # stack is empty
        return self.__stack[-1]
