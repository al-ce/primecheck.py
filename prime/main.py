"""A CLI tool to check if a number is prime and to list the first n primes."""

import argparse
from colorama import Fore
from collections.abc import Generator
from math import sqrt

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


def factorization(n: int) -> list:
    """Get all the factors of an integer"""

    if n == 0:
        return [0]

    factors = [n]
    if n < 1:
        n *= -1
        factors = [-1, n]

    s = sqrt(n).__floor__()
    for i in range(2, s+1):
        if n % i == 0:
            factors.append(i)
            if (q := n // i) != i:
                factors.append(q)

    factors.sort()
    return factors


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
        bound = int(sqrt(i)) + 1
        for j in range(3, bound, 2):
            if (i % j) == 0:
                break
        else:
            yield i
    print()


def integer_dict(integers: list) -> dict:
    """Return a dict of integers. Their value is a dict of their factors,
    their primality, and a string representation of the integer, colorized
    by primality."""

    return {
        n: {
            "str": f"{GREEN if is_prime(n) else RED}{n}{RESET}",
            "factors": factorization(n),
            # "is_prime": is_prime(n), # Not used
        }
        for n in integers
    }


def print_integers(integers: list, unsort: bool) -> str:
    """Print the given list of integers, colorized by primality, and their
    factors. Green for prime, red for composite."""

    integers if unsort else integers.sort()

    sorted_strs = sorted(
        [str(n) for n in integers],
        key=lambda x: len(str(x))
    )
    lls = len(longest_str := sorted_strs[-1])
    width = len(f"{RED}{longest_str}{RESET}")

    print("n".rjust(lls), " | factors")
    print("-" * (lls + 10))

    for k, v in integer_dict(integers).items():
        print(v["str"].rjust(width), " |", *v["factors"])


def print_primes_to_n(n: int) -> None:
    """Print the first n primes."""

    print(f"Prime numbers up to {n}:")
    for i, prime in enumerate(fast_primes(n), start=1):
        print(f"{prime}".rjust(len(str(n))), end=" ")
        if i % 10 == 0:
            print()


def main():
    args = parser.parse_args()
    n = args.nth
    integers = args.integers
    unsortFlag = args.unsortFlag

    print()
    print_integers(integers, unsortFlag) if integers else None
    print_primes_to_n(n) if n else None


if __name__ == "__main__":
    main()
