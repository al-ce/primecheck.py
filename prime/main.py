"""A CLI tool to check if a number is prime and to list the first n primes."""

import argparse
from colorama import Fore
from collections.abc import Generator
import math

GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET

parser = argparse.ArgumentParser()

parser.add_argument(
    "integers",
    default=[],
    help="Primality check for one or more integers, printed back to you",
    metavar="N",
    nargs='*',
    type=int,
)
parser.add_argument(
    "--n", "-N",
    default=0,
    dest="nth",
    help="Print all primes up to n.\n$ pprime --n 10",
    required=False,
    type=int,
)
parser.add_argument(
    "--u", "-U",
    dest="unsortFlag",
    help="Flag to keep your list of integers unsorted",
    action="store_true",
)


def is_prime(n: int) -> bool:
    """Check if a number is prime."""

    if n <= 3:
        return n > 1

    if n % 2 == 0 or n % 3 == 0:
        return False

    # All primes > 3 are of the form 6k ± 1, where k is an integer > 0
    for i in range(5, int(n**0.5) + 1, 6):
        # i = 6k - 1, i + 2 = 6k + 1
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def fast_primes(max_n: int) -> Generator[int, None, None]:
    """https://github.com/TheAlgorithms/Python/blob/master/maths/prime_numbers.py"""  # noqa
    numbers: Generator = (i for i in range(1, (max_n + 1), 2))
    if max_n > 2:
        yield 2
    for i in (n for n in numbers if n > 1):
        bound = int(math.sqrt(i)) + 1
        for j in range(3, bound, 2):
            if (i % j) == 0:
                break
        else:
            yield i
    print()


def print_checked_primes(integers: list, unsort: bool) -> str:
    """Print the given list of integers, colorized by primality.
    Green for prime, red for composite."""

    if not integers:
        return

    integers.sort() if not unsort else integers

    width = len(f"{RED}{max(integers)}{RESET}")

    for i, n in enumerate(integers, start=1):
        color = GREEN if is_prime(n) else RED
        print(f"{color}{n}{RESET}".rjust(width), end=" ")
        if i % 5 == 0 and i > 1:
            print()
        elif i == len(integers):
            print()


def print_primes_to_n(n: int) -> None:
    """Print the first n primes."""

    if not n:
        return

    print(f"Prime numbers up to {n}:")
    for i, prime in enumerate(fast_primes(n), start=1):
        print(f"{prime}".rjust(len(str(n))), end=" ")
        if i % 10 == 0:
            print()


def main():
    args = parser.parse_args()
    n = args.nth
    unsortFlag = args.unsortFlag
    print()
    print_checked_primes(args.integers, unsortFlag)
    print_primes_to_n(n)


if __name__ == "__main__":
    main()
