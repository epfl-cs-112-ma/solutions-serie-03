import pytest

from linkedlist import LinkedList

def test_basic_empty() -> None:
    empty = LinkedList()
    assert empty.is_empty
    with pytest.raises(ValueError):
        empty.head
    with pytest.raises(ValueError):
        empty.tail

def test_basic_non_empty() -> None:
    non_empty = LinkedList().prepend(5)
    assert not non_empty.is_empty
    assert non_empty.head == 5
    assert non_empty.tail.is_empty

    assert not non_empty.prepend(6).tail.is_empty

def test_eq() -> None:
    assert LinkedList() == LinkedList()
    assert LinkedList() != LinkedList().prepend(1)
    assert LinkedList().prepend(1) == LinkedList().prepend(1)
    assert LinkedList().prepend(1) != LinkedList()
    assert LinkedList().prepend(1).prepend(2) == LinkedList().prepend(1).prepend(2)
    assert LinkedList().prepend(1).prepend(2) != LinkedList().prepend(3).prepend(2)

def test_iteration() -> None:
    linked_list = LinkedList().prepend(5).prepend(4).prepend(3)
    result = []
    for i in range(len(linked_list)):
        result.append(linked_list[i])
    assert result == [3, 4, 5]
