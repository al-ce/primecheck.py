from operator import mul
from functools import reduce
from primes import primes_list
from prime.main import (
    is_prime, fast_primes, factorization, prime_factorization
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
