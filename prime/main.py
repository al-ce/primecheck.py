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
    help="Primality check for one or more integers",
    metavar="N",
    nargs='*',
    type=int,
)
parser.add_argument(
    "--n",
    default=0,
    dest="nth",
    help="Limit of the first n primes to be printed. Max 10_000.",
    required=False,
    type=int,
)


def is_prime(n: int) -> bool:
    """Check if a number is prime."""

    # 2 and 3 are prime, and any number < 2 is not prime
    if n <= 3:
        return n > 1

    # Even numbers and multiples of 3 are not prime
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


def print_colorized_ints(integers: list) -> str:
    """Print the given list of integers, colorized by primality.
    Green for prime, red for composite."""

    if not integers:
        return

    width = len(f"{RED}{max(integers)}{RESET}")

    for n in integers:
        color = GREEN if is_prime(n) else RED
        print(f"{color}{n}{RESET}".rjust(width))


def print_primes_to_n(n: int) -> None:
    """Print the first n primes."""

    if not n:
        return

    print(f"\nFirst {n} primes:")
    for i, prime in enumerate(fast_primes(n), start=1):
        print(f"{prime}".rjust(len(str(n))), end=" ")
        if i % 10 == 0:
            print()
    print()


class Test:
    # Uses a copy of https://primes.utm.edu/lists/small/10000.txt
    from .primes import primes_list
    primes = primes_list

    def test_prime_check(self):
        for n in self.primes:
            assert is_prime(n)

    def test_composites(self):
        for n in range(1, 10000):
            if n not in self.primes:
                assert not is_prime(n)

        for n in self.primes:
            assert not is_prime(n * 2)

    def test_zero_and_one(self):
        assert not is_prime(0)
        assert not is_prime(1)

    def test_prime_generator(self):
        fast_primes_list = list(fast_primes(self.primes[-1]))

        for n in fast_primes_list:
            assert is_prime(n)

        assert fast_primes_list == self.primes


def main():
    args = parser.parse_args()
    n = args.nth
    print_colorized_ints(args.integers)
    print_primes_to_n(n)


if __name__ == "__main__":
    main()
