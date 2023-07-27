"""A CLI tool to check if a number is prime and to list the first n primes."""

import argparse
from colorama import Fore
from collections.abc import Generator
from functools import reduce
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
parser.add_argument(
    "--g", "-G",
    dest="groupFlag",
    help="Flag to group your list of integers by their factors",
    action="store_true",
)
parser.add_argument(
    "--p", "-P",
    dest="primeFlag",
    help="Flag to print prime factors of your list of integers",
    action="store_true",
)
parser.add_argument(
    "-rs",
    dest="radical",
    help="Simplify the nth root of n by factoring out any perfects squares",
    nargs=2,
)


def colorize(text, color):
    """Colorize text."""
    color_code = getattr(Fore, color.upper())
    return color_code + text + Fore.RESET


def line_break():
    """Print a line break."""
    print()


def factorization(n: int, groupFlag: bool) -> list:
    """Get all the factors of an integer"""

    if n == 0:
        return [0]
    if n < 1:
        n *= -1

    s = sqrt(n).__floor__()

    factors = sorted([(i, n//i) for i in range(2, s+1) if n % i == 0])

    if groupFlag:
        return factors

    return sorted(set([i for tup in factors for i in tup]))


def prime_factorization(n):
    """Return the prime factors of a number."""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
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
    line_break()


def integer_dict(integers: list, groupFlag: bool, pf_flag: bool) -> dict:
    """Return a dict of integers. Their value is a dict of their factors,
    their primality, and a string representation of the integer, colorized
    by primality."""

    return {
        n: {
            "str": f"{GREEN if is_prime(n) else RED}{n}{RESET}",
            "factors":
                prime_factorization(n) if pf_flag
                else factorization(n, groupFlag)
        }
        for n in integers
    }


def integer_sorter(integers: list, unsort: bool) -> list:
    """Sort the given list of integers, or return it unsorted if the
    unsort flag is set."""
    integers if unsort else integers.sort()
    return integers


def print_integers(int_dict: dict, lls: int, width: int):
    """Print the given list of integers, colorized by primality, and their
    factors. Green for prime, red for composite."""

    line_break()
    print("n".rjust(lls), "| factors")
    print("-" * (lls + 10))

    for _, v in int_dict.items():
        print(v["str"].rjust(width), "|", *v["factors"])


def print_primes_to_n(n: int) -> None:
    """Print the first n primes."""

    print(f"\nPrime numbers up to {colorize(str(n), 'cyan')}:")
    for i, prime in enumerate(fast_primes(n), start=1):
        print(f"{prime}".rjust(len(str(n))), end=" ")
        if i % 10 == 0:
            line_break()


def measure_width(integers: list) -> tuple[int, int]:
    """Get length of longest integer in list as a string and its length when
    colored by colorama.Fore.{color}"""
    sorted_strs = sorted(
        [str(n) for n in integers],
        key=lambda x: len(str(x))
    )
    lls = len(longest_str := sorted_strs[-1])
    width = len(colorize(longest_str, "red"))
    return lls, width


def nth_root(base: int, nth: int) -> float:
    """Return the nth root of a number."""
    return base ** (1 / nth)


def factor_radical(base: int, nth: int) -> list:
    """Factor out perfect squares from the nth root of n."""

    if is_prime(base):
        return [radterm_str(base, nth)]

    factors = [(1, base)] + factorization(base, True)
    for f1, f2 in factors:
        # Prevent infinite recursion
        if f1 == 1:
            continue

        f1_rad, f2_rad = nth_root(f1, nth), nth_root(f2, nth)
        if f1 ** nth == base:
            return [f1]
        elif f1_rad % 1 == 0:
            return [f1_rad] + factor_radical(f2, nth)
        elif f2_rad % 1 == 0:
            return [f2_rad] + factor_radical(f1, nth)

    return [radterm_str(base, nth)]


def get_product(factors: list) -> int | None:
    if not factors:
        return None
    return int(reduce(lambda x, y: x * y, factors))


def combine_like_terms(factors: list) -> str:
    """Multiply the coefficients of a list of factors. Returns the product of
    the coefficients and the other elements of the list as a joined string."""

    coefficient = get_product(
        [f for f in factors if isinstance(f, (int, float))]
    )
    if coefficient is None:
        coefficient = ""

    other_terms = [f for f in factors if not isinstance(f, (int, float))]

    return str(coefficient) + "".join(other_terms)


def radterm_str(base: int, nth: int) -> str:
    """Format the nth root of base as a string."""
    # return f"{base} ** (1/{nth})"
    return f"(root({nth}){base})"


def print_simplified_radical(radical_term: list):
    """Print the simplified nth root of base."""
    nth, base = map(int, radical_term)
    result = combine_like_terms(factor_radical(base, nth))

    col_base, col_nth, col_equal, col_result = [
        colorize(str(x), color)
        for x, color in zip(
            [base, nth, "=", result],
            ["cyan", "yellow", "magenta", "green"]
        )
    ]

    line_break()
    print(f"{radterm_str(col_base, col_nth)} {col_equal} {col_result}")


def main():
    args = parser.parse_args()
    integers, n, unsortFlag, groupFlag, pfFlag, radical = vars(args).values()

    if sorted_ints := integer_sorter(integers, unsortFlag):
        int_dict = integer_dict(sorted_ints, groupFlag, pfFlag)
        lls, width = measure_width(sorted_ints)
        print_integers(int_dict, lls, width)

    print_primes_to_n(n) if n else None
    print_simplified_radical(radical) if radical else None


if __name__ == "__main__":
    main()
