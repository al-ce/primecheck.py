from operator import mul
from functools import reduce
from primes import primes_list
from prime.main import (
    is_prime, fast_primes, factorization, prime_factorization,
    get_product, factor_radical, radterm_str, combine_like_terms
)


class Test:
    # Uses a copy of https://primes.utm.edu/lists/small/10000.txt
    primes = primes_list

    def test_prime_check(self):
        for n in self.primes:
            assert is_prime(n)

    def test_zero_and_one(self):
        assert not is_prime(0)
        assert not is_prime(1)

    def test_prime_factorization(self):
        for n in self.primes:
            assert prime_factorization(n) == [n]

        for n in range(2, self.primes[500]):
            if is_prime(n):
                continue

            prime_factors_of_n = prime_factorization(n)

            for pf in prime_factors_of_n:
                assert is_prime(pf)

    def test_composites(self):
        for n in range(1, 10000):
            if n not in self.primes:
                assert not is_prime(n)

        for n in self.primes:
            assert not is_prime(n * 2)

    def test_factors_of_primes(self):
        for n in self.primes:
            assert not factorization(n, True)
            assert not factorization(n, False)

    def test_factors_of_composites(self,):
        for n in range(2, self.primes[500]):
            if is_prime(n):
                continue

            grouped_factors = factorization(n, True)
            ungrouped_factors = factorization(n, False)
            assert grouped_factors
            assert ungrouped_factors

            prime_factors_of_n = prime_factorization(n)
            expected_product = reduce(mul, prime_factors_of_n)

            for f in grouped_factors:
                assert n % f[0] == 0
                assert n % f[1] == 0
                assert f[0] * f[1] == expected_product

            for f in ungrouped_factors:
                assert n % f == 0
                assert all(p in ungrouped_factors for p in prime_factors_of_n)

    def test_prime_generator(self):
        nth = self.primes[5]
        fast_primes_list = list(fast_primes(nth))

        for n in fast_primes_list:
            assert is_prime(n)

        limit = self.primes.index(nth) + 1
        assert fast_primes_list == self.primes[:limit]

    def test_get_product(self):
        for i in range(2, 100):
            for j in range(2, 100):
                assert get_product([i, j]) == i * j
                assert get_product([-i, -j]) == i * j
                assert not get_product([i, -j]) == i * j

    def test_factor_radical(self):
        rad_terms = [(base, exp) for base in range(2, 10)
                     for exp in range(2, 10)]

        # e.g. sqrt(4**2) = 4, root3(7**3) = 7, etc.
        for base, nth in rad_terms:
            rad = base ** nth
            assert get_product(factor_radical(rad, nth)) == base

            # primes can't be factored further, so expected output is
            # e.g. factor_radical(7, 2) = (root(2)7))
            if is_prime(base):
                expected_string = radterm_str(base, nth)
                assert factor_radical(base, nth)[0] == expected_string

        # Test some known values with multiple terms
        known_simplifications = [
            (2, 28, "2", 7),
            (2, 60, "2", 15),
            (2, 120, "2", 30),
            (2, 45, "3", 5),
            (2, 54, "3", 6),
            (2, 99, "3", 11),
            (2, 32, "4", 2),
            (2, 50, "5", 2),
            (2, 75, "5", 3),
            (2, 243, "9", 3),
            (2, 700, "10", 7),
            (3, 32, "2", 4),
            (3, 54, "3", 2),
        ]
        for nth, old_base, coeff, new_base in known_simplifications:
            output = combine_like_terms(factor_radical(old_base, nth))
            expected = coeff + radterm_str(new_base, nth)
            assert output == expected
