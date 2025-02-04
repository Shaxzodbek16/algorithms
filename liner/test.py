from liner.liner import linear_search


def test_linear_search():
    # Standard cases (unsorted lists)
    assert linear_search([4, 2, 5, 1, 3], 3) == 4
    assert linear_search([5, 3, 1, 4, 2], 5) == 0
    assert linear_search([2, 4, 1, 5, 3], 1) == 2
    assert linear_search([4, 2, 5, 1, 3], 6) == -1  # Not found case

    # Negative numbers (unsorted)
    assert linear_search([-3, -5, 2, 0, -1, 4], -3) == 0
    assert linear_search([2, 4, -5, 0, -3, -1], 0) == 3
    assert linear_search([4, -1, 2, -3, 0, -5], 5) == -1  # Not found case

    # Floating point numbers (unsorted)
    assert linear_search([3.4, 0.1, 4.5, 1.2, 2.3], 2.3) == 4
    assert linear_search([4.5, 1.2, 3.4, 2.3, 0.1], 3.5) == -1  # Not found case

    # Strings (unsorted)
    assert linear_search(["banana", "fig", "cherry", "apple", "date"], "cherry") == 2
    assert linear_search(["date", "fig", "apple", "banana", "cherry"], "apple") == 2
    assert (
        linear_search(["fig", "banana", "cherry", "apple", "date"], "grape") == -1
    )  # Not found case

    # Single element list
    assert linear_search([10], 10) == 0
    assert linear_search([10], 5) == -1  # Not found case

    # Empty list
    assert linear_search([], 10) == -1  # Always not found

    # Large numbers (unsorted)
    assert linear_search([300, 500, 100, 200, 400], 400) == 4
    assert linear_search([100, 400, 200, 500, 300], 600) == -1  # Not found case


def main():
    test_linear_search()
    print("All tests passed!")


if __name__ == "__main__":
    main()
