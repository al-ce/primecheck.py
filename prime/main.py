"""A CLI tool to check if a number is prime and to list the first n primes."""

import argparse
from colorama import Fore

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


def print_colorized_ints(integers: list) -> str:
    """Print the given list of integers, colorized by primality.
    Green for prime, red for composite."""

    if not integers:
        return

    width = len(f"{RED}{max(integers)}{RESET}")

    for n in integers:
        color = GREEN if is_prime(n) else RED
        print(f"{color}{n}{RESET}".rjust(width))


def main():
    args = parser.parse_args()
    # n = args.nth
    print_colorized_ints(args.integers)


if __name__ == "__main__":
    main()
