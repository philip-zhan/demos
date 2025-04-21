import math


def sieve_of_eratosthenes(limit):
    """
    Generates prime numbers up to a given limit using the Sieve of Eratosthenes algorithm.

    Args:
        limit: The upper bound (inclusive) for finding prime numbers.

    Returns:
        A list of prime numbers up to the limit.
    """
    if limit < 2:
        return []

    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[p]:
            # Mark multiples of p as not prime
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False

    primes = [i for i, is_p in enumerate(is_prime) if is_p]
    return primes
