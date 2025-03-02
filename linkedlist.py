from __future__ import annotations

from dataclasses import dataclass
from types import NotImplementedType
from typing import Final

@dataclass(frozen=True)
class Node:
    head: int
    tail: Node | None

class LinkedList:
    __data: Final[Node | None]

    def __init__(self, data: Node | None = None) -> None:
        """Constructs a new empty list.

        The parameter `data` should not be provided by user code. It is
        reserved for internal use.
        """
        # Note: this modeling with a private-but-not-really parameter is not
        # great, but that's the best I could come up with, given Python's constraints.
        self.__data = data

    def __repr__(self) -> str:
        return f"LinkedList({repr(self.__data)})"

    def __str__(self) -> str:
        result = "["
        for i in range(len(self)):
            result += f"{self[i]}, "
        result += "]"
        return result

    @property
    def is_empty(self) -> bool:
        return self.__data is None

    @property
    def head(self) -> int:
        if self.__data is None:
            raise ValueError("head of empty list")
        return self.__data.head

    @property
    def tail(self) -> LinkedList:
        if self.__data is None:
            raise ValueError("tail of empty list")
        return LinkedList(self.__data.tail)

    def prepend(self, x: int) -> LinkedList:
        return LinkedList(Node(x, self.__data))

    def __eq__(self, other: object) -> bool | NotImplementedType:
        match other:
            case LinkedList():
                return (self.is_empty == other.is_empty) and \
                    (self.is_empty or (self.head == other.head and self.tail == other.tail))
            case _:
                return NotImplemented

    def __len__(self) -> int:
        if self.is_empty:
            return 0
        else:
            return 1 + len(self.tail)

    def __getitem__(self, i: int) -> int:
        if i == 0:
            return self.head
        else:
            return self.tail[i - 1]
