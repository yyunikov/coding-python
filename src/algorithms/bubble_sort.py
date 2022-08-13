from typing import List


def bubble_sort(n: List[int]):
    for i in range(0, len(n)):
        for j in range(i, len(n)):
            if n[j] < n[i]:
                tmp = n[i]
                n[i] = n[j]
                n[j] = tmp

    return n
