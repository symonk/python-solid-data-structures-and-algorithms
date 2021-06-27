import random
import typing


def built_in(arr: typing.List[int], target: int) -> int:
    """
    A simple solution using python built in functionality of the List class.
    Retrieves the (first) index of target.
    :param arr: The (sorted) sequence of integers.
    :param target: The target number to retrieve the index of.
    :return: the index of target; or -1 if target is not `in` arr.
    """
    try:
        return arr.index(target)
    except ValueError:
        return -1


def binary_search(arr: typing.List[int], target: int) -> int:
    """
    Performs a binary search through arr.  Divide and conquer the list to achieve
    o(log n) performance.  Pre requisites are that `arr` must be already sorted.
    :param arr: The (sorted) sequence of integers.
    :param target: The target number to retrieve the index of.
    :return: the index of target; or -1 if target is not `in` arr.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        pivot = (right + left) // 2
        value = arr[pivot]
        if value == target:
            return pivot
        elif value < target:
            left = pivot + 1
        else:
            right = pivot - 1
    return -1


if __name__ == "__main__":
    seq, find = list(range(0, 250_000, 3)), random.choice(range(250_000))
    assert binary_search(seq, find) == built_in(seq, find)