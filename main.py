class Deque:
    """
    Represents a double-ended queue (deque).

    This class provides an implementation of a deque where elements can be
    added or removed from both ends. It also provides utility methods to check
    for emptiness, access the size of the deque, peek at elements at either end
    without removal, and display the elements of the deque.

    :ivar elements: Internal storage for the elements in the deque.
    :type elements: list
    """
    def __init__(self):
        self.elements = []

    def add_first(self, item):
        self.elements.append(item)

    def add_last(self, item):
        self.elements.insert(0, item)

    def remove_first(self):
        item = self.elements.pop()
        return item

    def remove_last(self):
        item = self.elements.pop(0)
        return item

    def is_empty(self):
        if len(self.elements) > 0:
            return False
        return True

    def size(self):
        return len(self.elements)

    def peek_first(self):
        return self.elements[-1]

    def peek_last(self):
        return self.elements[0]

    def display_deque(self):
        print('\t | \t'.join(str(item) for item in self.elements))


def is_palindrome(word):
    """
    Checks if the given string is a palindrome.

    A palindrome is a word that reads the same forward and backward. This function
    uses a deque structure to verify if the characters in the string are arranged
    in a palindromic order.

    :param word: The string to evaluate for palindromic properties.
    :type word: str
    :return: True if the given string is a palindrome, otherwise False.
    :rtype: bool
    """
    deque = Deque()
    for char in word:
        deque.add_first(char)
    while deque.size() > 1:
        # Pop from the rear of the deque. Replace None with code
        first = deque.remove_first()
        # Pop from the front of the deque. Replace None with code
        last = deque.remove_last()
        # If statement goes below to check for equality

        if (first != last):
            return False
        return True


deque = Deque()
print(is_palindrome('alskjfwi'))
print(is_palindrome('level'))
print(is_palindrome('kayak'))