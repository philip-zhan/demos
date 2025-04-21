import argparse
from prime_lib import sieve_of_eratosthenes


def main():
    parser = argparse.ArgumentParser(
        description="Generate prime numbers up to a specified limit using the Sieve of Eratosthenes."
    )
    parser.add_argument(
        "limit", type=int, help="The upper limit for finding primes (inclusive)."
    )

    args = parser.parse_args()

    if args.limit < 2:
        print("Please provide a limit greater than or equal to 2.")
        return

    prime_numbers = sieve_of_eratosthenes(args.limit)

    print(f"Prime numbers up to {args.limit}:")
    print(prime_numbers)


if __name__ == "__main__":
    main()
