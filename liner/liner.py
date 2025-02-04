from typing import TypeVar

T = TypeVar("T")


def linear_search(array: list[T], target: T) -> int:
    for i in array:
        if i == target:
            return array.index(i)
    return -1


# Time complexity: O(n)
# Space complexity: O(1)
