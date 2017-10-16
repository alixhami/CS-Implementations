# Defines a node in the singly linked list
class Node:
    # allow external entities to read value but not write
    # allow external entities to read or write next node

    def __init__(self, value):
        self._data = value
        self.next = None

    @property
    def data(self):
        return self._data

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        # keep the head private. Not accessible outside this class
        self._head = None

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    def insert(self, value):
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node

    # method to print all the values in the linked list
    def visit(self):
        current = self._head
        while current is not None:
            print("%s " % current.data, end='')
            current = current.next

    # method that returns the length of the singly linked list
    def length(self):
        total = 0
        current = self._head
        while current is not None:
            total += 1
            current = current.next
        return total

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    def search(self, value):
        current = self._head
        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        current = self._head
        maximum = current.data
        while current is not None:
            if current.data > maximum:
                maximum = current.data
            current = current.next
        return maximum

    # method to return the min value in the linked list
    # returns the data value and not the node
    def find_min(self):
        current = self._head
        minimum = current.data
        while current is not None:
            if current.data < minimum:
                minimum = current.data
            current = current.next
        return minimum

    # method to return the value of the nth element from the beginning
    # assume indexing starts at 0 while counting to n
    def find_nth_from_beginning(self, n):
        if n >= self.length():
            raise IndexError('linked list element out of range')
        index = 0
        current = self._head
        while current is not None:
            if index == n:
                return current.data
            index += 1
            current = current.next

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    def find_nth_from_end(self, n):
        index = self.length() - 1
        current = self._head
        while index != n:
            current = current.next
            index -= 1
        return current.data

    # returns the value at the middle element in the singly linked list
    def find_middle_value(self):
        middle = self.length() // 2
        return self.find_nth_from_beginning(middle)

    # method to insert a new node with specific data value, assuming the linked
    # list is sorted in ascending order
    def insert_ascending(self, value):
        prev = self._head
        current = prev.next
        if value <= prev.data:
            self.insert(value)
            return
        new_node = Node(value)
        while current is not None:
            if value <= current.data:
                new_node.next = current
                prev.next = new_node
                return
            elif current.next == None:
                current.next = new_node
                return
            prev, current = current, current.next

    # method to delete the first node found with specified value
    def delete(self, value):
        prev = self._head
        current = self._head.next
        while current is not None:
            if current.data == value:
                prev.next = current.next
                del current
                return
            prev = current
            current = current.next
        raise ValueError('value not found')

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    def reverse(self):
        temp = self._head.next
        self._head.next = None
        while temp is not None:
          current = temp
          temp = temp.next
          self._head, self._head.next = current, self._head

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    def has_cycle(self):
        slow = fast = self._head
        while True:
            slow = slow.next
            if fast.next is None:
                return False
            else:
                fast = fast.next.next

            if slow is None or fast is None:
                return False
            elif slow == fast:
                return True

    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        # don't do anything if the linked list is empty
        if self._head is None:
            return

        # navigate to last node
        current = self._head
        while current.next is not None:
            current = current.next

        current.next = self._head # make the last node link to first node
