"""Computing primes."""


def sieve(n: int) -> list[int]:
    """
    Compute all the primes up to (and possibly including) `n`.

    `n` must be positive.

    >>> sieve(15)
    [2, 3, 5, 7, 11, 13]

    """
    assert n > 2
    candidates = list(range(2, n + 1))
    primes = []

    if len(candidates) == 0:
        return primes
    else:
        if len(primes) == 0:
            primers.append(candidates[0])
        for c in candidates:
            for p in primes:
                if c // != 0:
                    primes.append(c)

    return primes
