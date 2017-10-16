import pytest
from linked_list import Node, LinkedList


def test_create_node():
    new_node = Node(4)

    assert new_node.data == 4
    assert new_node.next is None

def test_node_set_next():
    first_node = Node(4)
    second_node = Node(5)

    first_node.next = second_node

    assert first_node.next.data == 5

def test_node_cant_reset_data():
    new_node = Node(4)

    with pytest.raises(AttributeError):
        new_node.data = 6

def test_insert():
    my_linked_list = LinkedList()
    to_insert = [5, 3, 1]
    for value in to_insert:
        my_linked_list.insert(value)

    to_insert.reverse()
    current = my_linked_list._head
    for i in range(len(to_insert)):
        assert current.data == to_insert[i]
        current = current.next

def test_visit(capfd):
    my_linked_list = LinkedList()
    to_insert = [5, 3, 1]
    for value in to_insert:
        my_linked_list.insert(value)

    my_linked_list.visit()

    out, err = capfd.readouterr()
    assert out == "1 3 5 "

def test_visit_empty(capfd):
    my_linked_list = LinkedList()

    my_linked_list.visit()

    out, err = capfd.readouterr()
    assert out == ""

def test_length():
    my_linked_list = LinkedList()
    to_insert = [5, 3, 1]
    for value in to_insert:
        my_linked_list.insert(value)

    assert my_linked_list.length() == 3

def test_search():
    my_linked_list = LinkedList()
    to_insert = [5, 3, 1]
    for value in to_insert:
        my_linked_list.insert(value)

    for value in to_insert:
        assert my_linked_list.search(value) is True
    assert my_linked_list.search(6) is False

def test_maximum():
    my_linked_list = LinkedList()
    to_insert = [6, 5, 4, 3, 1]
    for value in to_insert:
        my_linked_list.insert(value)

    assert my_linked_list.find_max() == 6

def test_minimum():
    my_linked_list = LinkedList()
    to_insert = [6, 5, 4, 3, 1]
    for value in to_insert:
        my_linked_list.insert(value)

    assert my_linked_list.find_min() == 1

def test_nth_from_beginning():
    my_linked_list = LinkedList()
    to_insert = [6, 5, 4, 3, 1]
    for value in to_insert:
        my_linked_list.insert(value)

    to_insert.reverse()
    for i in range(len(to_insert)):
        assert my_linked_list.find_nth_from_beginning(i) == to_insert[i]

def test_nth_from_end():
    my_linked_list = LinkedList()
    to_insert = [6, 5, 4, 3, 1]
    for value in to_insert:
        my_linked_list.insert(value)

    for i in range(len(to_insert)):
        assert my_linked_list.find_nth_from_end(i) == to_insert[i]

def test_find_middle_value():
    my_linked_list = LinkedList()
    to_insert = [6, 5, 4, 3, 1]
    for value in to_insert:
        my_linked_list.insert(value)

    assert my_linked_list.find_middle_value() == 4

def test_insert_ascending():
    my_linked_list = LinkedList()
    to_insert = [5, 3, 1]
    for value in to_insert:
        my_linked_list.insert(value)

    my_linked_list.insert_ascending(4)
    my_linked_list.insert_ascending(6)
    my_linked_list.insert_ascending(0)

    expected = [0, 1, 3, 4, 5, 6]
    assert my_linked_list.length() == len(expected)
    for i in range(len(expected)):
        assert my_linked_list.find_nth_from_beginning(i) == expected[i]

def test_delete():
    my_linked_list = LinkedList()
    to_insert = [6, 5, 4, 3, 1]
    for value in to_insert:
        my_linked_list.insert(value)
    assert my_linked_list.length() == 5

    my_linked_list.delete(5)

    assert my_linked_list.length() == 4
    assert my_linked_list.search(5) is False

def test_delete_value_not_found():
    my_linked_list = LinkedList()
    to_insert = [6, 5, 4, 3, 1]
    for value in to_insert:
        my_linked_list.insert(value)

    with pytest.raises(ValueError):
        my_linked_list.delete(9)

def test_reverse():
    my_linked_list = LinkedList()
    to_insert = [6, 5, 4, 3, 1]
    for value in to_insert:
        my_linked_list.insert(value)

    my_linked_list.reverse()

    for i in range(len(to_insert)):
        assert my_linked_list.find_nth_from_beginning(i) == to_insert[i]

def test_has_cycle_false():
    my_linked_list = LinkedList()
    to_insert = [6, 5, 4, 3, 1]
    for value in to_insert:
        my_linked_list.insert(value)

    assert not my_linked_list.has_cycle()

def test_create_cycle():
    my_linked_list = LinkedList()
    to_insert = [6, 5, 4, 3, 1]
    for value in to_insert:
        my_linked_list.insert(value)

    my_linked_list.create_cycle()

    assert my_linked_list.has_cycle()
