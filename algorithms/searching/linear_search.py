import random
import typing


def linear_search(arr: typing.List[int], target: int) -> int:
    """
    Performs a linear search through arr.  This is O(N) as worst case the last element in arr
    will need to be checked
    :param arr: The sequence of integers
    :param target: The target number to retrieve the index of.
    :return: the index of target; or -1 if target is not `in` arr.
    """
    for idx, n in enumerate(arr):
        if n == target:
            return idx
    return -1


if __name__ == "__main__":
    seq, find = list(range(0, 250_000, 3)), random.choice(range(250_000))
    random.shuffle(seq)
    print(linear_search(seq, find))


