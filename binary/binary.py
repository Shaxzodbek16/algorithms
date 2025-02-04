from typing import Any, TypeVar

T = TypeVar("T")


def binary_search(array: list[T], target: T) -> int:
    l, r = 0, len(array) - 1

    while l <= r:
        m = (l + r) // 2
        if array[m] == target:
            return m
        if array[m] < target:
            l = m + 1
            continue
        r = m - 1
    return -1


# Time complexity: O(log n)
# Space complexity: O(1)
