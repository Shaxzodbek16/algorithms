from binary import binary_search


def test_binary_search():
    # Standard cases
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 5) == 4
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    assert binary_search([1, 2, 3, 4, 5], 6) == -1  # Not found case

    # Negative numbers
    assert binary_search([-5, -3, -1, 0, 2, 4], -3) == 1
    assert binary_search([-5, -3, -1, 0, 2, 4], 0) == 3
    assert binary_search([-5, -3, -1, 0, 2, 4], 5) == -1  # Not found case

    # Floating point numbers
    assert binary_search([0.1, 1.2, 2.3, 3.4, 4.5], 2.3) == 2
    assert binary_search([0.1, 1.2, 2.3, 3.4, 4.5], 3.5) == -1  # Not found case

    # Strings
    assert binary_search(["apple", "banana", "cherry", "date", "fig"], "cherry") == 2
    assert binary_search(["apple", "banana", "cherry", "date", "fig"], "apple") == 0
    assert (
        binary_search(["apple", "banana", "cherry", "date", "fig"], "grape") == -1
    )  # Not found case

    # Single element list
    assert binary_search([10], 10) == 0
    assert binary_search([10], 5) == -1  # Not found case

    # Empty list
    assert binary_search([], 10) == -1  # Always not found

    # Large numbers
    assert binary_search([100, 200, 300, 400, 500], 400) == 3
    assert binary_search([100, 200, 300, 400, 500], 600) == -1  # Not found case

    # Large list
    assert binary_search(list(range(1000000)), 999999) == 999999
    assert binary_search(list(range(1000000)), 1000000) == -1  # Not found case
    assert binary_search(list(range(1000000)), 0) == 0
    assert binary_search(list(range(1000000)), 500000) == 500000


def main():
    test_binary_search()
    print("All tests passed!")


if __name__ == "__main__":
    main()
