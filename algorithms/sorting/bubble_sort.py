from typing import List
import random

"""
Description:  Bubble sort involves iterating through a list comparing adjacent values and 'bubbling' the
higher of the two values to the top.
Performance: O(n2)
"""

def bubble_sort(arr: List[int]) -> None:
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                # swapping has occurred, swap items and set swapped back to True
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True


if __name__ == "__main__":
    from copy import deepcopy
    x = list(range(15))
    y = deepcopy(x)
    random.shuffle(x)
    bubble_sort(x)
    assert x == sorted(y)
