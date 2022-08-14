import functools
from typing import Dict

memo: Dict[int, int] = {}


def fib(n: int):
    if n == 0:
        return 0

    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    result = fib(n - 2) + fib(n - 1)

    memo[n] = result
    return result


@functools.lru_cache(None)
def fib_with_lru_cache(n: int):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n - 2) + fib(n - 1)
